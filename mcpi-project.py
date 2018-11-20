from mcpi.minecraft import Minecraft
mc = Minecraft.create("10.183.0.78", 4711)
x,y,z = mc.player.getPos()
mc.events.pollBlockHits()
STONE = 1
WOOD = 17
AIR = 0
WATER_FLOWING = 8
STAIRS_COBBLESTONE = 67
LAPIS_LAZULI_BLOCK = 22
BEDROCK = 7
STONE_SLAB = 44
STONE_SLAB_DOUBLE = 43
#CLEARED AREA
mc.setBlocks(x+50, y+50, z+50, x+1, y+1, z+1, AIR)
#BEDROCK_MIDDLE
mc.setBlocks(x+8, y+10, z+5, x+7, y+18, z+5, BEDROCK)
mc.setBlocks(x+8, y+9, z+5, x+7, y+17, z+5, BEDROCK)
mc.setBlocks(x+8, y+8, z+5, x+7, y+16, z+5, BEDROCK)
mc.setBlocks(x+8, y+7, z+5, x+7, y+15, z+5, BEDROCK)
mc.setBlocks(x+8, y+6, z+5, x+7, y+14, z+5, BEDROCK)
mc.setBlocks(x+8, y+5, z+5, x+7, y+13, z+5, BEDROCK)
mc.setBlocks(x+8, y+4, z+5, x+7, y+12, z+5, BEDROCK)
mc.setBlocks(x+8, y+3, z+5, x+7, y+11, z+5, BEDROCK)


#BEDROCK_TOP
mc.setBlocks(x+8, y+17, z+5, x+7, y+17, z+5, BEDROCK)
mc.setBlocks(x+8, y+17, z+5, x+7, y+17, z+5, BEDROCK)
mc.setBlocks(x+8, y+17, z+5, x+7, y+17, z+5, BEDROCK)
mc.setBlocks(x+8, y+17, z+5, x+7, y+17, z+5, BEDROCK)
mc.setBlocks(x+8, y+18, z+5, x+7, y+17, z+5, BEDROCK)
mc.setBlocks(x+8, y+18, z+5, x+7, y+17, z+5, BEDROCK)
mc.setBlocks(x+8, y+18, z+5, x+7, y+17, z+5, BEDROCK)

#stone slab/block LEFT
mc.setBlocks(x+10, y+18, z+5, x+10, y+18, z+5, STONE_SLAB)
mc.setBlocks(x+10, y+17, z+5, x+10, y+17, z+5, BEDROCK)
mc.setBlocks(x+11, y+17, z+5, x+11, y+17, z+5, STONE_SLAB_DOUBLE)
mc.setBlocks(x+12, y+17, z+5, x+12, y+17, z+5, STONE_SLAB)


#stone slab/block RIGHT
mc.setBlocks(x+5, y+17, z+5, x+5, y+17, z+5, STONE_SLAB)
mc.setBlocks(x+5, y+16, z+5, x+5, y+16, z+5, BEDROCK)
mc.setBlocks(x+4, y+16, z+5, x+4, y+16, z+5, STONE_SLAB_DOUBLE)
mc.setBlocks(x+3, y+16, z+5, x+3, y+16, z+5, STONE_SLAB)

#BEDROCK BOTTOM
mc.setBlocks(x+8, y+1, z+5, x+7, y+1, z+5, BEDROCK)
mc.setBlocks(x+8, y+0, z+5, x+7, y+0, z+5, BEDROCK)


#angle left
mc.setBlocks(x+13, y+11, z+5, x+21, y+11, z+5, STONE_SLAB)
mc.setBlocks(x+21, y+5, z+5, x+21, y+10, z+5, STONE_SLAB_DOUBLE)
mc.setBlocks(x+13, y+10, z+5, x+20, y+10, z+5, STONE)
mc.setBlocks(x+12, y+10, z+5, x+12, y+10, z+5, STONE_SLAB_DOUBLE)
mc.setBlocks(x+20, y+9, z+5, x+14, y+9, z+5, STONE)
mc.setBlocks(x+13, y+9, z+5, x+13, y+9, z+5, STONE_SLAB_DOUBLE)
mc.setBlocks(x+20, y+8, z+5, x+15, y+8, z+5, STONE)

pos = mc.player.getPos()
mc.player.setPos(x, y, z)
#Water = 8
#Air = 0
#API Blocks
#=======================
#AIR                   0
#STONE                 1
#GRASS                 2
#DIRT                  3
#COBBLESTONE           4
#WOOD_PLANKS           5
#SAPLING               6
#BEDROCK               7
#WATER_FLOWING         8
#WATER                 8
#WATER_STATIONARY      9
#LAVA_FLOWING         10
#LAVA                 10
#LAVA_STATIONARY      11
#SAND                 12
#GRAVEL               13
#GOLD_ORE             14
#IRON_ORE             15
#COAL_ORE             16
#WOOD                 17
#LEAVES               18
#GLASS                20
#LAPIS_LAZULI_ORE     21
#LAPIS_LAZULI_BLOCK   22
#SANDSTONE            24
#BED                  26
#COBWEB               30
#GRASS_TALL           31
#WOOL                 35
#FLOWER_YELLOW        37
#FLOWER_CYAN          38
#MUSHROOM_BROWN       39
#MUSHROOM_RED         40
#GOLD_BLOCK           41
#IRON_BLOCK           42
#STONE_SLAB_DOUBLE    43
#STONE_SLAB           44
#BRICK_BLOCK          45
#TNT                  46
#BOOKSHELF            47
#MOSS_STONE           48
#OBSIDIAN             49
#TORCH                50
#FIRE                 51
#STAIRS_WOOD          53
#CHEST                54
#DIAMOND_ORE          56
#DIAMOND_BLOCK        57
#CRAFTING_TABLE       58
#FARMLAND             60
#FURNACE_INACTIVE     61
#FURNACE_ACTIVE       62
#DOOR_WOOD            64
#LADDER               65
#STAIRS_COBBLESTONE   67
#DOOR_IRON            71
#REDSTONE_ORE         73
#SNOW                 78
#ICE                  79
#SNOW_BLOCK           80
#CACTUS               81
#CLAY                 82
#SUGAR_CANE           83
#FENCE                85
#GLOWSTONE_BLOCK      89
#BEDROCK_INVISIBLE    95
#STONE_BRICK          98
#GLASS_PANE          102
#MELON               103
#FENCE_GATE          107
#GLOWING_OBSIDIAN    246
#NETHER_REACTOR_CORE 247
