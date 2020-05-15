**Blocks**

A block is a fragment of data within a snapshot. Each snapshot can contain thousands of blocks. All blocks in a snapshot are of a fixed size.

---

**Block indexes**

A block index is the offset position of a block within a snapshot, and it is used to identify the block. Multiply the BlockIndex value with the BlockSize value (BlockIndex * BlockSize) to identify the logical offset of the data in the logical block.

---

**Block tokens**

A block token is the identifying hash of a block within a snapshot, and it is used to locate the block data.