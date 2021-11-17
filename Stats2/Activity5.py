import rasterio

dataset = rasterio.open("clipped")
band1 = dataset.read(1)

D = {}
for i in range(0, dataset.width):
  for j in range(0, dataset.height):
    if band1[j,i] not in D:
      D[band[j,i]] = 0
    D[band[j,i]] += 1
    
# Verification
# Last print statement should be true
sum = 0
for key in D:
  sum += D[key]
  
print(sum == dataset.width*dataset.height)
