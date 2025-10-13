import numpy as np

def computeReferenceTwist(u1, u2, t1, t2, refTwist):
  # Inputs:
  # refTwist is a guess solution. It can be set to zero
  ut = parallel_transport(u1, t1, t2)
  ut = rotateAxisAngle(ut, t2, refTwist)
  refTwist = refTwist + signedAngle(ut, u2, t2)
  return refTwist
