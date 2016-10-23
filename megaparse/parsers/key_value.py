# key=value parser, mirroring the same method in Ansible
# the upstream code is available at:
# https://github.com/ansible/ansible/blob/devel/lib/ansible/parsing/splitter.py

import re

_HEXCHAR = '[a-fA-F0-9]'
_ESCAPE_SEQUENCE_RE = re.compile(r'''
    ( \\U{0}           # 8-digit hex escapes
    | \\u{1}           # 4-digit hex escapes
    | \\x{2}           # 2-digit hex escapes
    | \\N\{{[^}}]+\}}  # Unicode characters by name
    | \\[\\'"abfnrtv]  # Single-character escapes
    )'''.format(_HEXCHAR*8, _HEXCHAR*4, _HEXCHAR*2), re.UNICODE | re.VERBOSE)

def _decode_escapes(s):
    def decode_match(match):
        return codecs.decode(match.group(0), 'unicode-escape')

    return _ESCAPE_SEQUENCE_RE.sub(decode_match, s)


def is_quoted(data):
    return len(data) > 1 and data[0] == data[-1] and data[0] in ('"', "'") and data[-2] != '\\'

def unquote(data):
    ''' removes first and last quotes from a string, if the string starts and ends with the same quotes '''
    if is_quoted(data):
        return data[1:-1]
    return data

def parse_kv(stream, check_raw=False):
    '''
    Convert a string of key/value items to a dict. If any free-form params
    are found and the check_raw option is set to True, they will be added
    to a new parameter called '_raw_params'. If check_raw is not enabled,
    they will simply be ignored.
    '''
    options = {}
    for orig_x in stream.splitlines():
        x = _decode_escapes(orig_x)
        if "=" in x:
            pos = 0
            try:
                while True:
                    pos = x.index('=', pos + 1)
                    if pos > 0 and x[pos - 1] != '\\':
                        break
            except ValueError:
                # ran out of string, but we must have some escaped equals,
                # so replace those and append this to the list of raw params
                raw_params.append(x.replace('\\=', '='))
                continue

            k = x[:pos]
            v = x[pos + 1:]


            # FIXME: make the retrieval of this list of shell/command
            #        options a function, so the list is centralized
            if check_raw and k not in ('creates', 'removes', 'chdir', 'executable', 'warn'):
                raw_params.append(orig_x)
            else:
                value = unquote(v.strip())
                try:
                    value = int(value)
                except:
                    try:
                        value = float(value)
                    except:
                        pass
                options[k.strip()] = value

        else:
            raise Exception()

    return options

