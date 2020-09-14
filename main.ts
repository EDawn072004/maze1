scene.setBackgroundColor(10)
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleBlueCrystal, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    game.over(true)
})
let mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
tiles.setTilemap(tiles.createTilemap(hex`
            1000100001030101010101010101010101010101010000000000000000000101010100010100010101010101010101000000000101000100000000000000000001010101010001000101010100010100000000010100010001010101000001000101000101000100000000000100010001010001010001010101010001000100010000010100010101010100010001000101000101000000000000000100010000010001010001010101000101000101010101010100010000010001010000000000010101000100010100010101010101000101010001000101000101010101010001010100010000000000000000000100020101010101010101010101010101010101
        `, img`
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
        `, [myTiles.transparency16, sprites.builtin.forestTiles10, sprites.dungeon.collectibleBlueCrystal, sprites.dungeon.collectibleInsignia], TileScale.Sixteen))
tiles.placeOnRandomTile(mySprite, sprites.dungeon.collectibleInsignia)
info.startCountdown(17)
scene.cameraFollowSprite(mySprite)
