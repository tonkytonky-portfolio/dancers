import random


class Dancer(object):
    def __init__(self, name):
        self.name = name
        self.sex = ''
        self.styles = []

    def __repr__(self):
        return self.name

    def can_dance(self, track):
        """
        Returns set of styles that the dancer can perform with the track.
        """
        return list(set(self.styles).intersection(track.styles))

    def perform_random_moves(self, track):
        """
        Chooses and prints random moves from random style, the dancer can dance to the track, is playing.
        """
        is_dancing = random.choice(self.can_dance(track))
        print('. '.join([
            "{0:s} is dancing {1:s}".format(self.name, is_dancing.name),
            ', '.join([
                "Head: {0:s}".format(random.choice(is_dancing.head)),
                "body: {0:s}".format(random.choice(is_dancing.body)),
                "arms: {0:s}".format(random.choice(is_dancing.arms)),
                "legs: {0:s}.".format(random.choice(is_dancing.legs))
            ])]))

    def drink_vodka(self):
        print("{0:s} is drinking vodka in the bar.".format(self.name))


class Style(object):
    """
    Stores a style's name and the lists of moves corresponding to head, body, arms and legs.
    """
    def __init__(self, name, head, body, arms, legs):
        self.name = name
        self.head = head
        self.body = body
        self.arms = arms
        self.legs = legs

    def __repr__(self):
        return self.name


class Track(object):
    """
    Stores a track's genre name and the list of styles, dancers perform to this genre.
    """
    def __init__(self, name, styles):
        self.name = name
        self.styles = styles

    def __repr__(self):
        return self.name


def _main():
    styles, tracks, max_styles, max_tracks = get_config()
    dancers = get_dancers(styles, max_styles)
    tracks = get_tracks(tracks, max_tracks)
    begin_party(dancers, tracks)


def get_config():
    # Restrictions of maximum number of styles, a dancer can knows
    # and maximum number of tracks, DJ can plays at a party.
    max_styles = 3
    max_tracks = 5

    hip_hop = Style(
        name="Hip-Hop",
        head=[
            'bounce back and forth',
            'bounce left and right',
            'stands still',
            'chicken head',
        ],
        body=[
            'bounce back and forth',
            'bounce left and right',
            'janet jackson',
            'brooklyn bounce',
        ],
        arms=[
            'bent at the elbow',
            'the wop',
            'harlem shake',
            'waves',
            'tutting',
        ],
        legs=[
            'half squat',
            'v-step',
            'running man',
            'kriss kross',
            'party machine',
            'steps',
        ]
    )
    rnb_dance = Style(
        name="R'n'B",
        head=[
            'smooth rolls',
            'stands still',
            'chicken head',
        ],
        body=[
            'bounce back and forth',
            'bounce left and right',
            'snake',
            'waves',
        ],
        arms=[
            'smooth waves',
            'tone wop',
            'move from the body',
        ],
        legs=[
            'half squat',
            'stomp',
            'smooth steps',
            'steps',
        ]
    )
    electrodance = Style(
        name="Electrodance",
        head=[
            'stands still',
            'turns left and right',
        ],
        body=[
            'bounce back and forth',
            'jerky moves',
        ],
        arms=[
            'big rolls',
            'small rolls',
            'force stops',
        ],
        legs=[
            'move to the rhythm',
            'stand still',
            'glides',
            'steps',
        ]
    )
    pop_dance = Style(
        name="Pop dance",
        head=[
            'smooth rolls',
            'stands still',
        ],
        body=[
            'smooth waves',
            'stands still',
        ],
        arms=[
            'smooth waves',
            'jerky moves',
            'doing a right hand finger',
            'doing a left hand finger',
            'going up',
        ],
        legs=[
            'smooth steps',
            'jerky steps',
        ]
    )
    house_dance = Style(
        name="House dance",
        head=[
            'move from the body',
            'stands still',
        ],
        body=[
            'jacking',
            'lofting',
            'jack-in-the-box',
        ],
        arms=[
            'move from the body',
            'jerky moves',
            'waves',
        ],
        legs=[
            'pas de bourree',
            'farmer',
            'train',
            'roller',
            'loose legs',
            'salsa steps',
            'steps',
            'floor spins',
        ]
    )

    styles = [
        hip_hop,
        rnb_dance,
        electrodance,
        pop_dance,
        house_dance
    ]
    tracks = [
        Track(name="R'n'B", styles=[hip_hop, rnb_dance]),
        Track(name="Electrohouse", styles=[electrodance, house_dance]),
        Track(name="Pop", styles=[pop_dance]),
        Track(name="House", styles=[house_dance, pop_dance]),
        Track(name="Hip-Hop", styles=[hip_hop, house_dance]),
    ]

    return styles, tracks, max_styles, max_tracks


def get_dancers(styles, max_styles):
    """
    Asks user to define an arbitrary number of dancers,
    watches on correctness of the input.
    Returns a list of Dancer objects.
    """
    print("### Let's create some dancers.")
    dancers = []
    dancer_index = 1
    while True:
        print()
        dancer_input = input(
            "Input Dancer's #{0:d} name or type "
            "\"done\" to continue: ".format(dancer_index)
        ).strip()

        # Exit case
        if dancer_input == 'done':
            if not dancers:
                print('You must input at least one Dancer!')
                continue
            break

        # Wrong input case
        elif len(dancer_input) == 0:
            print("Sorry, I don't get you.\n")

        # Continue case
        else:
            name = dancer_input
            dancer = Dancer(name)

            sex_input = input(
                "Choose {0:s}'s sex. Type \"m\" for male "
                "or \"f\" for female: ".format(dancer.name)
            ).strip()
            # Wrong input handling
            while sex_input != 'm' and sex_input != 'f':
                print("Sorry, I don't get you.\n")
                sex_input = input(
                    "Choose {0:s}'s sex. "
                    "Type \"m\" or \"f\": ".format(dancer.name)
                ).strip()
            dancer.sex = sex_input

            dancer_styles = styles[:]

            while True:
                # Restriction for a dancer
                if len(dancer.styles) < max_styles:
                    print(
                        "\n{0:s} knows {1:s}. "
                        "\nChoose {2:s} style for {3:s} from the list below "
                        "or type \"done\" to continue: ".format(
                            dancer.name,
                            ', '.join(
                                [style.name for style in dancer.styles]
                            ) if dancer.styles else 'nothing',
                            'a' if not dancer.styles else 'one more',
                            'him' if dancer.sex == 'm' else 'her'
                        ))
                    print(', '.join([
                        '{0:d}: {1:s}'.format(i, style.name)
                        for i, style in zip(range(1, len(dancer_styles) + 1), dancer_styles)
                    ]))
                    style_input = input().strip()
                # Continue if restriction is up
                else:
                    print("It's enough for one dancer. Continue...")
                    break

                # Exit case
                if style_input == 'done':
                    if not dancer.styles:
                        print('You must input at least one Style!')
                        continue
                    break

                # Continue case
                elif style_input.isdigit() and 1 <= int(style_input) <= len(dancer_styles):
                    dancer.styles.append(dancer_styles[int(style_input) - 1])
                    del dancer_styles[int(style_input) - 1]

                # Wrong input case
                else:
                    print("Sorry, I don't get you.\n")

            dancers.append(dancer)
            dancer_index += 1

    return dancers


def get_tracks(tracks, max_tracks):
    """
    Asks user to define an arbitrary number of tracks that will be
    played at the party, watches on correctness of the input.
    Returns a list of Track objects.
    """
    print("\n### Let's choose tracks to play at the club tonight.")
    party_tracks = []
    while True:
        # Restriction for a party
        if len(party_tracks) < max_tracks:
            print(
                '\nDJ will play {0:s}.'
                '\nChoose {1:s} track from the list below or type "done" '
                'to continue: '.format(
                    ', '.join(
                        [track.name for track in party_tracks]
                    ) if party_tracks else 'nothing',
                    'a' if not party_tracks else 'one more',
                )
            )
            print(', '.join([
                '{0:d}: {1:s}'.format(i, genre.name)
                for i, genre in zip(range(1, len(tracks) + 1), tracks)
            ]))
            track_input = input()

        # Continue if restriction is up
        else:
            print("It's enough for a party. Continue...")
            break

        # Exit case
        if track_input == 'done':
            if not party_tracks:
                print('You must input at least one Track!')
                continue
            break

        # Continue case
        elif track_input.isdigit() and 1 <= int(track_input) <= len(tracks):
            party_tracks.append(tracks[int(track_input) - 1])

        # Wrong input case
        else:
            print("Sorry, I don't get you.\n")

    return party_tracks


def begin_party(dancers, tracks):
    """
    Displays the track, currently being playing and the actions of the dancers.
    """
    print("\n### Let's start the party!")

    track_index = 0
    while True:
        # Continue case
        if 0 <= track_index < len(tracks):
            print("\nDJ is playing {0:s}.".format(tracks[track_index].name))
            for dancer in dancers:
                if dancer.can_dance(tracks[track_index]):
                    dancer.perform_random_moves(tracks[track_index])
                else:
                    dancer.drink_vodka()

            track_input = input(
                "\nPress \"n\" to swith to the next track and \"p\" "
                "to swith to the previous one: ").strip()
            if track_input == 'n':
                track_index += 1
            elif track_input == 'p':
                track_index -= 1

        # Continue case
        elif track_index < 0:
            print("\nPlay the first track again.")
            track_index = 0

        # Exit case
        elif track_index == len(tracks):
            print("\n### The party is over.")
            break

        # Wrong input case
        else:
            print("Sorry, I don't get you.\n")


if __name__ == '__main__':
    _main()
