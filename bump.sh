#!/usr/bin/env bash

NOT_CLEAN="$( bump2version patch \
    --dry-run --no-tag --no-commit --list 2>&1 >/dev/null \
    | grep "Git working directory is not clean" | head -1 \
    )"

if [[ -z "$NOT_CLEAN" ]]
then
    CUR_VER="$(bump2version patch \
        --dry-run --no-tag --no-commit --list \
        | grep current_version | sed -r s,"^.*=",, \
        )"
    printf "Current version is: "
    printf "$CUR_VER\n"
    CUR_VER_DATE="$(echo "$CUR_VER" | cut -d. -f-3)"

    NEW_VER="$(bump2version patch \
        --dry-run --no-tag --no-commit --list \
        | grep new_version | sed -r s,"^.*=",, \
        )"
    NEW_VER_DATE="$(echo "$NEW_VER" | cut -d. -f-3)"

    echo "CUR_VER_DATE"
    echo "$CUR_VER_DATE"
    echo "NEW_VER_DATE"
    echo "$NEW_VER_DATE"

    if [[ "$CUR_VER_DATE" == "$NEW_VER_DATE" ]]
    then
        printf "Date is the same and new version will be: "
    else
        NEW_VER="$NEW_VER_DATE.1"
        printf "Date is different and new version will be: "
    fi
    printf "$NEW_VER\n"

    read -p "Proceed with tag? " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        RESULT="$(bump2version patch --new-version ${NEW_VER}  2>&1 >/dev/null)"
        if [[ -z "$RESULT" ]]
        then
            echo "Tag was created"
        else
            echo "$RESULT"
        fi
    fi
else
    echo "Please commit before bump!"
fi

