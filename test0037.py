import asyncio

# 異步後台任務
async def background_task():
    while True:
        print("後台任務正在執行...")
        await asyncio.sleep(5)  # 每 5 秒執行一次

# 主程序
async def main():
    # 啟動後台任務
    task = asyncio.create_task(background_task())
    
    try:
        while True:
            print("主程式正在運行...")
            await asyncio.sleep(2)  # 主程式每 2 秒執行一次
    except KeyboardInterrupt:
        print("程式已被手動中止")
        task.cancel()  # 取消後台任務

# 執行主程序
asyncio.run(main())
