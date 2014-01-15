# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.
# See the file LICENSE.pyloxi which should have been included in the source distribution

# Automatically generated by LOXI from template module.py
# Do not modify

import struct
import loxi
import const
import common
import action
import instruction
import oxm
import action_id
import instruction_id
import meter_band
import bsn_tlv
import util
import loxi.generic_util

class bsn_tlv(loxi.OFObject):
    subtypes = {}

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!H', 0)
        try:
            subclass = bsn_tlv.subtypes[subtype]
        except KeyError:
            raise loxi.ProtocolError("unknown bsn_tlv subtype %#x" % subtype)
        return subclass.unpack(reader)


class idle_notification(bsn_tlv):
    type = 7

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = idle_notification()
        _type = reader.read("!H")[0]
        assert(_type == 7)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length - (2 + 2))
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("idle_notification {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn_tlv.subtypes[7] = idle_notification

class idle_time(bsn_tlv):
    type = 5

    def __init__(self, value=None):
        if value != None:
            self.value = value
        else:
            self.value = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!Q", self.value))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = idle_time()
        _type = reader.read("!H")[0]
        assert(_type == 5)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length - (2 + 2))
        obj.value = reader.read("!Q")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.value != other.value: return False
        return True

    def pretty_print(self, q):
        q.text("idle_time {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("value = ");
                q.text("%#x" % self.value)
            q.breakable()
        q.text('}')

bsn_tlv.subtypes[5] = idle_time

class ipv4(bsn_tlv):
    type = 4

    def __init__(self, value=None):
        if value != None:
            self.value = value
        else:
            self.value = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.value))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = ipv4()
        _type = reader.read("!H")[0]
        assert(_type == 4)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length - (2 + 2))
        obj.value = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.value != other.value: return False
        return True

    def pretty_print(self, q):
        q.text("ipv4 {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("value = ");
                q.text(util.pretty_ipv4(self.value))
            q.breakable()
        q.text('}')

bsn_tlv.subtypes[4] = ipv4

class mac(bsn_tlv):
    type = 1

    def __init__(self, value=None):
        if value != None:
            self.value = value
        else:
            self.value = [0,0,0,0,0,0]
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!6B", *self.value))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = mac()
        _type = reader.read("!H")[0]
        assert(_type == 1)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length - (2 + 2))
        obj.value = list(reader.read('!6B'))
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.value != other.value: return False
        return True

    def pretty_print(self, q):
        q.text("mac {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("value = ");
                q.text(util.pretty_mac(self.value))
            q.breakable()
        q.text('}')

bsn_tlv.subtypes[1] = mac

class port(bsn_tlv):
    type = 0

    def __init__(self, value=None):
        if value != None:
            self.value = value
        else:
            self.value = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(util.pack_port_no(self.value))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = port()
        _type = reader.read("!H")[0]
        assert(_type == 0)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length - (2 + 2))
        obj.value = util.unpack_port_no(reader)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.value != other.value: return False
        return True

    def pretty_print(self, q):
        q.text("port {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("value = ");
                q.text(util.pretty_port(self.value))
            q.breakable()
        q.text('}')

bsn_tlv.subtypes[0] = port

class rx_packets(bsn_tlv):
    type = 2

    def __init__(self, value=None):
        if value != None:
            self.value = value
        else:
            self.value = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!Q", self.value))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = rx_packets()
        _type = reader.read("!H")[0]
        assert(_type == 2)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length - (2 + 2))
        obj.value = reader.read("!Q")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.value != other.value: return False
        return True

    def pretty_print(self, q):
        q.text("rx_packets {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("value = ");
                q.text("%#x" % self.value)
            q.breakable()
        q.text('}')

bsn_tlv.subtypes[2] = rx_packets

class tx_packets(bsn_tlv):
    type = 3

    def __init__(self, value=None):
        if value != None:
            self.value = value
        else:
            self.value = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!Q", self.value))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = tx_packets()
        _type = reader.read("!H")[0]
        assert(_type == 3)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length - (2 + 2))
        obj.value = reader.read("!Q")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.value != other.value: return False
        return True

    def pretty_print(self, q):
        q.text("tx_packets {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("value = ");
                q.text("%#x" % self.value)
            q.breakable()
        q.text('}')

bsn_tlv.subtypes[3] = tx_packets

class vlan_vid(bsn_tlv):
    type = 6

    def __init__(self, value=None):
        if value != None:
            self.value = value
        else:
            self.value = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!H", self.value))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = vlan_vid()
        _type = reader.read("!H")[0]
        assert(_type == 6)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length - (2 + 2))
        obj.value = reader.read("!H")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.value != other.value: return False
        return True

    def pretty_print(self, q):
        q.text("vlan_vid {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("value = ");
                q.text("%#x" % self.value)
            q.breakable()
        q.text('}')

bsn_tlv.subtypes[6] = vlan_vid

