SELECT CONCAT ('/home/grep/src/' , f.BOARD_ID, '/' , FILE_ID, FILE_NAME,FILE_EXT) as FILE_PATH
FROM USED_GOODS_FILE f
WHERE f.BOARD_ID = (SELECT b.BOARD_ID
                    FROM USED_GOODS_BOARD b
                    ORDER BY b.VIEWS DESC
                    LIMIT 1)
ORDER BY f.FILE_ID DESC