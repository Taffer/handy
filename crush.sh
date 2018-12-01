#! /bin/bash
#
# Use pngcrush -brute to find the smallest possible size for a given PNG file,
# replacing the original with the smaller version.

t="0"
for f in "$@" ; do
    pngcrush -brute "$f" "${f}.crushed" > /dev/null 2>&1
    if [ ! -e "${f}.crushed" ] ; then
        echo "$f is not a PNG file."
    else
        ns="$(stat -c '%s' "${f}.crushed")"
        os="$(stat -c '%s' "$f")"
        if [[ "$ns" -lt "$os" ]] ; then
            ds="$(("$os" - "$ns"))"
            echo "$f - Saved: $ds bytes"
            mv "$f" "${f}.orig" && mv "${f}.crushed" "$f" && rm "${f}.orig"
            t="$(("$t" + "$ds"))"
        else
            rm "${f}.crushed"
        fi
    fi
done

echo "Total saved: $t bytes"
