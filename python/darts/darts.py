"""Calculate Darts Score"""

# The Bullseye is the origin of the coordinate grid
BULLSEYE: tuple[int, int] = (0, 0)

# Coordinates with radious <= these enumerated values counts as being
# within the corresponding circle.  Coordiantes with radius > 10 units
# miss the target completely.

INNERCIRCLE: int = 1      
MIDDLECIRCLE: int = 5
OUTERCIRCLE: int = 10

# Scoring System
INNERCIRCLESCORE: int = 10
MIDDLECIRCLESCORE: int = 5
OUTERCIRCLESCORE: int = 1
MISSEDTARGETCOMPLETELY: int = 0

def score(x: int, y: int) -> int:
    """Calculate score for a dart located at the point defined by x,y

    :param x: the location horizontally relative to the bullseye
    :type x: int
    :param y: the location vertically relative to the bullsyeye
    :type y: int
    :return: the number of points for landing at the coordinates
    :rtype: int
    """
    pass
