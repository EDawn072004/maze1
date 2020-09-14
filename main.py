scene.set_background_color(10)
def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_blue_crystal,
    on_overlap_tile)

mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . 3 . 3 3 . 3 . . . . . . 
            . . . . 3 3 3 3 3 3 . . . . . . 
            . . . . 1 1 1 1 1 d . . . . . . 
            . . . . 1 d 1 d 1 d . . . . . . 
            . . . . 1 1 d 1 1 d . . . . . . 
            . . . . 1 1 1 1 1 d . . . . . . 
            . . . . . 1 d 1 d . . . . . . . 
            . . . 1 1 3 3 3 3 1 1 . . . . . 
            . . . . . . 3 3 . . . . . . . . 
            . . . . . . 3 3 . . . . . . . . 
            . . . . . 3 3 3 3 . . . . . . . 
            . . . . . 3 3 3 3 . . . . . . . 
            . . . . . 1 . . 1 . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
tiles.set_tilemap(tiles.create_tilemap(hex("""
            1000100001030101010101010101010101010101010000000000000000000101010100010100010101010101010101000000000101000100000000000000000001010101010001000101010100010100000000010100010001010101000001000101000101000100000000000100010001010001010001010101010001000100010000010100010101010100010001000101000101000000000000000100010000010001010001010101000101000101010101010100010000010001010000000000010101000100010100010101010101000101010001000101000101010101010001010100010000000000000000000100020101010101010101010101010101010101
        """),
        img("""
            2 . 2 2 2 2 2 2 2 2 2 2 2 2 2 2
            2 . . . . . . . . . 2 2 2 2 . 2
            2 . 2 2 2 2 2 2 2 2 2 . . . . 2
            2 . 2 . . . . . . . . . 2 2 2 2
            2 . 2 . 2 2 2 2 . 2 2 . . . . 2
            2 . 2 . 2 2 2 2 . . 2 . 2 2 . 2
            2 . 2 . . . . . 2 . 2 . 2 2 . 2
            2 . 2 2 2 2 2 . 2 . 2 . 2 . . 2
            2 . 2 2 2 2 2 . 2 . 2 . 2 2 . 2
            2 . . . . . . . 2 . 2 . . 2 . 2
            2 . 2 2 2 2 . 2 2 . 2 2 2 2 2 2
            2 . 2 . . 2 . 2 2 . . . . . 2 2
            2 . 2 . 2 2 . 2 2 2 2 2 2 . 2 2
            2 . 2 . 2 2 . 2 2 2 2 2 2 . 2 2
            2 . 2 . . . . . . . . . 2 . . 2
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        """),
        [myTiles.transparency16,
            sprites.builtin.forest_tiles10,
            sprites.dungeon.collectible_blue_crystal,
            sprites.dungeon.collectible_insignia],
        TileScale.SIXTEEN))
tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)
info.start_countdown(17)
scene.camera_follow_sprite(mySprite)
