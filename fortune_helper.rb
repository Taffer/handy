#!/usr/bin/ruby
#
# This is a helper so you can call fortune from JWZ's xscreensaver
# port to OS X.  It starts an http server and all it does is return
# fortune.  Its pretty stupid overall.

require 'webrick'
require 'stringio'
require 'logger'
require 'optparse'

class FortuneServlet < WEBrick::HTTPServlet::AbstractServlet
  def do_GET(request, response)
    response.status = 200
    response['Content-Type'] = 'text/plain'
    response.body = get_fortune
  end

  def get_fortune
    out = StringIO.new
    IO.popen(@@command) { |f| f.each_line { |l| out << l } }
    return out.string
  end

  def FortuneServlet.set_fortune_command(command)
    @@command = command
  end
end

#FortuneServlet.set_fortune_command('/opt/local/bin/fortune -s')
FortuneServlet.set_fortune_command('/usr/bin/fortune -s')

port = '8080'
opts = OptionParser.new
opts.on('-c COMMAND', 'Use this fortune command') do |val|
  FortuneServlet.set_fortune_command(val)
end
opts.on('-p PORT', 'Use this port') { |val| port = val }
opts.on('-h', '--help', 'Show this message') do
  puts opts
  exit
end
opts.parse(ARGV)
opts = nil

null_logger = Logger.new('/dev/null')
config = {
  :BindAddress => '127.0.0.1',
  :Port => port,
  :Logger => null_logger,
  :AccessLog => null_logger
}
server = WEBrick::HTTPServer.new(config)
server.mount("/", FortuneServlet)

# trap signals to invoke the shutdown procedure cleanly
['INT', 'TERM'].each { |signal| trap(signal){ server.shutdown } }

server.start
