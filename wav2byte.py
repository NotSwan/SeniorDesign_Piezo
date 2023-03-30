import wave

with wave.open("allstars.wav","r") as f:
    params = f.getparams()
    frames = f.readframes(1000000)

print(params)

f = open("allstarsBytes", "a")

for frame in frames:
    f.write(str(hex(frame)) + "\n")