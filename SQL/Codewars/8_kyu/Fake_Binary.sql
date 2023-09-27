SELECT
  x,
  TRANSLATE(x, '123456789', '000011111')
    AS res 
FROM fakebin
