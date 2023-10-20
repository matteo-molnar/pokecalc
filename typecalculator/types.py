# Pokemon Type Constants


NORMAL = "NORMAL"
FIRE = "FIRE"
WATER = "WATER"
ELECTRIC = "ELECTRIC"
GRASS = "GRASS"
ICE = "ICE"
FIGHTING = "FIGHTING"
POISON = "POISON"
GROUND = "GROUND"
FLYING = "FLYING"
PSYCHIC = "PSYCHIC"
BUG = "BUG"
ROCK = "ROCK"
GHOST = "GHOST"
DRAGON = "DRAGON"
DARK = "DARK"
STEEL = "STEEL"
FAIRY = "FAIRY"


type_tuple = (
    NORMAL,
    FIRE,
    WATER,
    ELECTRIC,
    GRASS,
    ICE,
    FIGHTING,
    POISON,
    GROUND,
    FLYING,
    PSYCHIC,
    BUG,
    ROCK,
    GHOST,
    DRAGON,
    DARK,
    STEEL,
    FAIRY,
)

ineffective_against = {
    NORMAL: (GHOST,),
    FIRE: (),
    WATER: (),
    ELECTRIC: (GROUND,),
    GRASS: (),
    ICE: (),
    FIGHTING: (GHOST,),
    POISON: (STEEL,),
    GROUND: (FLYING,),
    FLYING: (),
    PSYCHIC: (DARK,),
    BUG: (),
    ROCK: (),
    GHOST: (NORMAL,),
    DRAGON: (FAIRY,),
    DARK: (),
    STEEL: (),
    FAIRY: (),
}

not_very_effective_against = {
    NORMAL: (
        ROCK,
        STEEL,
    ),
    FIRE: (
        FIRE,
        WATER,
        ROCK,
    ),
    WATER: (
        WATER,
        GRASS,
        DRAGON,
    ),
    ELECTRIC: (
        ELECTRIC,
        GRASS,
        DRAGON,
    ),
    GRASS: (
        FIRE,
        GRASS,
        POISON,
        FLYING,
        BUG,
        DRAGON,
        STEEL,
    ),
    ICE: (
        FIRE,
        WATER,
        ICE,
        STEEL,
    ),
    FIGHTING: (
        POISON,
        FLYING,
        PSYCHIC,
        BUG,
        FAIRY,
    ),
    POISON: (
        POISON,
        GROUND,
        ROCK,
        GHOST,
    ),
    GROUND: (
        GRASS,
        BUG,
    ),
    FLYING: (
        ELECTRIC,
        ROCK,
        STEEL,
    ),
    PSYCHIC: (
        PSYCHIC,
        STEEL,
    ),
    BUG: (
        FIRE,
        FIGHTING,
        POISON,
        FLYING,
        GHOST,
        STEEL,
        FAIRY,
    ),
    ROCK: (
        FIGHTING,
        GROUND,
        STEEL,
    ),
    GHOST: (DARK,),
    DRAGON: (STEEL,),
    DARK: (
        FIGHTING,
        DARK,
        FAIRY,
    ),
    STEEL: (
        FIRE,
        WATER,
        ELECTRIC,
        STEEL,
    ),
    FAIRY: (
        FIRE,
        POISON,
        STEEL,
    ),
}

super_effective_against = {
    NORMAL: (),
    FIRE: (
        GRASS,
        ICE,
        BUG,
        STEEL,
    ),
    WATER: (
        FIRE,
        GROUND,
        ROCK,
    ),
    ELECTRIC: (
        WATER,
        FLYING,
    ),
    GRASS: (
        WATER,
        GROUND,
        ROCK,
    ),
    ICE: (
        GRASS,
        GROUND,
        FLYING,
        DRAGON,
    ),
    FIGHTING: (
        NORMAL,
        ICE,
        DARK,
        STEEL,
    ),
    POISON: (
        GRASS,
        FAIRY,
    ),
    GROUND: (
        FIRE,
        ELECTRIC,
        POISON,
        ROCK,
        STEEL,
    ),
    FLYING: (
        GRASS,
        FIGHTING,
        BUG,
    ),
    PSYCHIC: (
        FIGHTING,
        POISON,
    ),
    BUG: (
        GRASS,
        PSYCHIC,
        DARK,
    ),
    ROCK: (
        FIRE,
        ICE,
        FLYING,
        BUG,
    ),
    GHOST: (
        PSYCHIC,
        GHOST,
    ),
    DRAGON: (DRAGON,),
    DARK: (
        PSYCHIC,
        GHOST,
    ),
    STEEL: (
        ICE,
        ROCK,
        FAIRY,
    ),
    FAIRY: (
        FIGHTING,
        DRAGON,
        DARK,
    ),
}

# FOR COPYING
DEFAULT_TYPE_DICT: dict[str, set] = {
    NORMAL: set(),
    FIRE: set(),
    WATER: set(),
    ELECTRIC: set(),
    GRASS: set(),
    ICE: set(),
    FIGHTING: set(),
    POISON: set(),
    GROUND: set(),
    FLYING: set(),
    PSYCHIC: set(),
    BUG: set(),
    ROCK: set(),
    GHOST: set(),
    DRAGON: set(),
    DARK: set(),
    STEEL: set(),
    FAIRY: set(),
}
