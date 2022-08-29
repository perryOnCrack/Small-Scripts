import uuid

guid = uuid.uuid4()

print(guid)
print(str(guid).upper())
print('{ 0x%08X, 0x%04X, 0x%04X, { 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X, 0x%02X }}'
     % (guid.time_low,
        guid.time_mid,
        guid.time_hi_version,
        guid.clock_seq_hi_variant,
        guid.clock_seq_low,
        0xff & (guid.node >> 40),
        0x00ff & (guid.node >> 32),
        0x0000ff & (guid.node >> 24),
        0x000000ff & (guid.node >> 16),
        0x00000000ff & (guid.node >> 8),
        0x0000000000ff & (guid.node >> 0))
    )
