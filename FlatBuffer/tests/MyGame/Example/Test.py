# automatically generated, do not modify

# namespace: Example

import flatbuffers

class Test(object):
    __slots__ = ['_tab']

    # Test
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Test
    def A(self): return self._tab.Get(flatbuffers.number_types.Int16Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # Test
    def B(self): return self._tab.Get(flatbuffers.number_types.Int8Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(2))

def CreateTest(builder, a, b):
    builder.Prep(2, 4)
    builder.Pad(1)
    builder.PrependInt8(b)
    builder.PrependInt16(a)
    return builder.Offset()
