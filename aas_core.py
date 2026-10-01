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

operational_data_reference = aas_types.Reference (
    type = aas_types.ReferenceTypes.MODEL_REFERENCE,
    keys = [
        aas_types.Key(
            type=aas_types.KeyTypes.SUBMODEL,
            value= operational_data.id
        )
    ]
)

asset_information = aas_types.AssetInformation(
    asset_kind=aas_types.AssetKind.INSTANCE,
    global_asset_id="urn:example:machine-01"
)

machine_aas = aas_types.AssetAdministrationShell(
    id="urn:example:machine-01:aas",
    id_short="Machine01AAS",
    
    asset_information=asset_information,
    
    submodels=[operational_data_reference]
)

print(operational_data.id)
print(operational_data.id_short)

for element in operational_data.submodel_elements:
    print(element.id_short, element.value)
    
print(machine_aas.id)
print(machine_aas.id_short)
print(machine_aas.asset_information.global_asset_id)

for reference in machine_aas.submodels:
    for key in reference.keys:
        print(key.type, key.value)