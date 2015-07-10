def isBlocked(mapObj, gameStateObj, x, y):
    if isWall(mapObj, x, y):
        return True
    elif x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return True
    elif (x, y) in gameStateObj['stars']:
        return True
    return False
    
def drawMap(mapObj, gameStateObj, goals):
    mapSurfWidth = len(mapObj) * TILEWIDTH
    mapSurfHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR)
    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if mapObj[x][y] in TILEMAPPING:
                baseTile = TILEMAPPING[mapObj[x][y]]
            elif mapObj[x][y] in OUTSIDEDECOMAPPING:
                baseTile = TILEMAPPING[' ']
             mapSurf.blit(baseTile, spaceRect)

            if mapObj[x][y] in OUTSIDEDECOMAPPING:
               mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)
            elif (x, y) in gameStateObj['stars']:
                if (x, y) in goals:
                    mapSurf.blit(IMAGESDICT['covered goal'], spaceRect)
                mapSurf.blit(IMAGESDICT['star'], spaceRect)
            elif (x, y) in goals:
                mapSurf.blit(IMAGESDICT['uncovered goal'], spaceRect)
            if (x, y) == gameStateObj['player']:
                mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)

    return mapSurf


def isLevelFinished(levelObj, gameStateObj):
    for goal in levelObj['goals']:
        if goal not in gameStateObj['stars']:
            return False
    return True


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
