"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature in kelvin.
    :param neutrons_emitted: int or float - neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The neutrons emitted per second is greater than 500.
    - temperature * neutrons emitted per second less than 500000.
    """
    critical_temperature = temperature < 800
    critical_neutrons = neutrons_emitted > 500
    critical_reaction = (temperature * neutrons_emitted) < 500000

    return critical_temperature and critical_neutrons and critical_reaction


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage.
    :param current: int or float - current.
    :param theoretical_max_power: int or float - power when efficiency is 100%.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    efficiency = generated_power / theoretical_max_power * 100

    if efficiency >= 80.0:
        return 'green'
    elif efficiency >= 60.0 and efficiency < 80.0:
        return 'orange'
    elif efficiency >= 30.0 and efficiency < 60.0:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    pass
