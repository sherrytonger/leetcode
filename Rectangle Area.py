__author__ = 'Sherry'

# find the total area covered by two rectilinear rectangles in a 2D plane
# only two scenarios:overlapping and non-overlaping
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        S=(C-A)*(D-B) + (G-E)*(H-F)
        # non-overlapping
        if A>G or C<E or D<F or B>H :
            return S
        # overlapping
        else:
            s_common=(min(C,G)-max(A,E))*(min(D,H)-max(B,F))
            return S-s_common

sol = Solution()
print sol.computeArea(-2, -2, 2, 2, -3, -3, 3, -1)
