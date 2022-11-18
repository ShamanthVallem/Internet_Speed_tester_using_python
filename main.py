import speedtest

test = speedtest.Speedtest()
print("Loadings servers")
test.get_servers()
print("Aceesing best server")
best = test.get_best_server()
# print(best)
print(f"Found best server: {best['host']} located in {best['country']}")

print("Performing Download test")
download_result = test.download()
print("Performing upload test")
upload_result = test.upload()
ping_result = test.results.ping

print(f"Download-speed: {download_result/1024/1024:.2f} Mbps")
print(f"Upload-speed: {upload_result/1024/1024:.2f} Mbps")
print(f"Ping: {ping_result:.2f} ms")