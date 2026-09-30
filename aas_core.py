from machine import machine
import aas_core3.types as aas_types

temperature_property = aas_types.Property(
    id_short="Temperature",
    value=str(machine.temperature),
    value_type=aas_types.DataTypeDefXSD.DOUBLE
    )

rpm_property = aas_types.Property(
    id_short="RPM",
    value=str(machine.rpm),
    value_type=aas_types.DataTypeDefXSD.INT
)

running_property = aas_types.Property(
    id_short="Running",
    value=str(machine.running).lower(),
    value_type=aas_types.DataTypeDefXSD.BOOLEAN
)

max_temperature_property = aas_types.Property(
    id_short="MaxTemperature",
    value=str(machine.max_temperature),
    value_type=aas_types.DataTypeDefXSD.DOUBLE
)

max_RPM_property = aas_types.Property(
    id_short="MaxRPM",
    value=str(machine.max_rpm),
    value_type=aas_types.DataTypeDefXSD.INT
)