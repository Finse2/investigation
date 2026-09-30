from machine import Machine
import aas_core3.types as aas_types

machine = Machine("Machine-01")

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


operational_data = aas_types.Submodel(
    id ="urn:example:machine-01:operational-data",
    id_short="OperationalData",

    submodel_elements= [
        temperature_property,
        rpm_property,
        running_property,
        max_temperature_property,
        max_RPM_property
    ]
)

print(operational_data.id)
print(operational_data.id_short)

for element in operational_data.submodel_elements:
    print(element.id_short, element.value)