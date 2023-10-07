SELECT dna, TRANSLATE(dna, 'ACTG', 'TGAC') AS res
  FROM dnastrand;