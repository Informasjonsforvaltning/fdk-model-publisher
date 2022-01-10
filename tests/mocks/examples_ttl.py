"""Example TTL output."""
# flake8: noqa

ex_1_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom> a modelldcatno:ObjectType ;
    dct:title "Eiendom"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstatter>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstattetav>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#nummer>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstatter> a modelldcatno:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstattetav> a modelldcatno:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#nummer> a modelldcatno:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_2_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#EiendomResultat> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#EiendomResultat> a modelldcatno:ObjectType ;
    dct:title "EiendomResultat"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#code>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#data>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#message> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#int32> a modelldcatno:SimpleType ;
    dct:title "int32"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#integerschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstatter> a modelldcatno:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstattetav> a modelldcatno:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#nummer> a modelldcatno:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#int32> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#data> a modelldcatno:Role ;
    dct:title "data"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#message> a modelldcatno:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom> a modelldcatno:ObjectType ;
    dct:title "Eiendom"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstatter>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstattetav>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#nummer>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_3_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Kommune>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SÃ¸k> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#SÃ¸k> a modelldcatno:ObjectType ;
    dct:title "SÃ¸k"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SÃ¸k#code>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SÃ¸k#data>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SÃ¸k#message> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date> a modelldcatno:SimpleType ;
    dct:title "date"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#int32> a modelldcatno:SimpleType ;
    dct:title "int32"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#integerschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstatter> a modelldcatno:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstattetav> a modelldcatno:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#nummer> a modelldcatno:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#fylke> a modelldcatno:Attribute ;
    dct:title "fylke"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#gyldigtil> a modelldcatno:Attribute ;
    dct:title "gyldigtil"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#navn> a modelldcatno:Attribute ;
    dct:title "navn"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SÃ¸k#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#int32> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SÃ¸k#data> a modelldcatno:Choice ;
    dct:title "data"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSome <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Kommune> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/SÃ¸k#message> a modelldcatno:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom> a modelldcatno:ObjectType ;
    dct:title "Eiendom"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstatter>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstattetav>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#nummer>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Kommune> a modelldcatno:ObjectType ;
    dct:title "Kommune"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#fylke>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#gyldigtil>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#navn>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_4_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#EiendomResultat>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Kommune>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#KommuneResultat>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Søk> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#EiendomResultat> a modelldcatno:ObjectType ;
    dct:title "EiendomResultat"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#code>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#data>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#message> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#KommuneResultat> a modelldcatno:ObjectType ;
    dct:title "KommuneResultat"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat#code>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat#data>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat#message> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Søk> a modelldcatno:ObjectType ;
    dct:title "Søk"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Søk#code>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Søk#data>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Søk#message> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date> a modelldcatno:SimpleType ;
    dct:title "date"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#integer> a modelldcatno:SimpleType ;
    dct:title "integer"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#integerschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstatter> a modelldcatno:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstattetav> a modelldcatno:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#nummer> a modelldcatno:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#int32> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#data> a modelldcatno:Role ;
    dct:title "data"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/EiendomResultat#message> a modelldcatno:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#fylke> a modelldcatno:Attribute ;
    dct:title "fylke"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#gyldigtil> a modelldcatno:Attribute ;
    dct:title "gyldigtil"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#date> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#navn> a modelldcatno:Attribute ;
    dct:title "navn"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#int32> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat#data> a modelldcatno:Composition ;
    dct:title "data"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data#data> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat#message> a modelldcatno:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data#data> a modelldcatno:ObjectType ;
    dct:title "data"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data/data#erstatter>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data/data#erstattetav>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data/data#kommune> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data/data#erstatter> a modelldcatno:Role ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Kommune> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data/data#erstattetav> a modelldcatno:Role ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data/data/erstattetav#erstattetav> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data/data#kommune> a modelldcatno:Role ;
    dct:title "kommune"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Kommune> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data/data/erstattetav#erstattetav> a modelldcatno:ObjectType ;
    dct:title "erstattetav"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data/data/erstattetav/erstattetav#id> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/KommuneResultat/data/data/erstattetav/erstattetav#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#integer> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Søk#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#int32> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Søk#data> a modelldcatno:Choice ;
    dct:title "data"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSome <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Kommune> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Søk#message> a modelldcatno:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Eiendom> a modelldcatno:ObjectType ;
    dct:title "Eiendom"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstatter>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#erstattetav>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#nummer>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Eiendom#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#int32> a modelldcatno:SimpleType ;
    dct:title "int32"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#integerschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Kommune> a modelldcatno:ObjectType ;
    dct:title "Kommune"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#fylke>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#gyldigtil>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#id>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#navn>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Kommune#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_5_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Account>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#AccountStatus>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#FinancialInstitution> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Account> a modelldcatno:ObjectType ;
    dct:description "Account: a specification of a clearly defined type of financial events"@en ;
    dct:title "Account"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Account#servicer>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Account#status> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Account#servicer> a modelldcatno:Composition ;
    dct:description "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account"@en ;
    dct:title "servicer"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#FinancialInstitution> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Account#status> a modelldcatno:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> ;
    modelldcatno:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#AccountStatus> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/FinancialInstitution#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/FinancialInstitution/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/FinancialInstitution/name#name> a modelldcatno:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#AccountStatus> a modelldcatno:CodeList ;
    dct:title "AccountStatus"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#FinancialInstitution> a modelldcatno:ObjectType ;
    dct:description "financial institution: Business or other institution involved in finance and banking"@en ;
    dct:title "FinancialInstitution"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/FinancialInstitution#name> .
"""

ex_6_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#ObjA>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#ObjC>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#ObjD>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<http://uri.com.well-known/skolem/0> a modelldcatno:Role ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#ObjC> .

<http://uri.com.well-known/skolem/1> a modelldcatno:Role ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#ObjD> .

<http://uri.com.well-known/skolem/2> a modelldcatno:Attribute ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<http://uri.com.well-known/skolem/3> a modelldcatno:Attribute ;
    dct:description "test f"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#ObjA> a modelldcatno:ObjectType ;
    dct:description "Root A"@en ;
    dct:title "ObjA"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ObjA#objB> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ObjA#objB> a modelldcatno:Composition ;
    dct:description "b thing"@en ;
    dct:title "objB"@en ;
    modelldcatno:contains <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ObjA/objB#objB> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/ObjA/objB#objB> a modelldcatno:ObjectType ;
    modelldcatno:hasProperty <http://uri.com.well-known/skolem/0>,
        <http://uri.com.well-known/skolem/1>,
        <http://uri.com.well-known/skolem/2>,
        <http://uri.com.well-known/skolem/3> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#ObjC> a modelldcatno:ObjectType ;
    dct:description "test c"@en ;
    dct:title "ObjC"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#ObjD> a modelldcatno:ObjectType ;
    dct:description "test d"@en ;
    dct:title "ObjD"@en .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_7_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Balance>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#BalanceType> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Balance> a modelldcatno:ObjectType ;
    dct:description "Balance: Sum of deposits and loans in the financial account"@en ;
    dct:title "Balance"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Balance#type> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Balance#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> ;
    modelldcatno:hasValueFrom <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#BalanceType> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#BalanceType> a modelldcatno:CodeList ;
    dct:description "Balance type"@en ;
    dct:title "BalanceType"@en .
"""

ex_8_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Amount>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#CounterParty>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Transaction>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#TransactionReference> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Transaction> a modelldcatno:ObjectType ;
    dct:description "Transaction: any posting on an account"@en ;
    dct:title "Transaction"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#additionalInfo>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#amount>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#counterParties>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#merchant>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#references>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#transactionIdentifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/CounterParty#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/CounterParty/name#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/CounterParty/name#name> a modelldcatno:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#additionalInfo> a modelldcatno:Attribute ;
    dct:description "'Additional information on a transaction: textual description of the contents of a transaction'"@en ;
    dct:title "additionalInfo"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction/additionalInfo#additionalInfo> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#amount> a modelldcatno:Attribute ;
    dct:title "amount"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Amount> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#counterParties> a modelldcatno:Role ;
    dct:description "Counterparty: another party, the party to whom a transaction is going or coming from"@en ;
    dct:title "counterParties"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#CounterParty> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#merchant> a modelldcatno:Attribute ;
    dct:description "User location: the physical location of the transaction"@en ;
    dct:title "merchant"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction/merchant#merchant> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#references> a modelldcatno:Role ;
    dct:description "Transaction reference: unique reference associated with the transaction"@en ;
    dct:title "references"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#TransactionReference> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction#transactionIdentifier> a modelldcatno:Attribute ;
    dct:description "Transaction Identifier: The identifier for the transaction"@en ;
    dct:title "transactionIdentifier"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction/transactionIdentifier#transactionIdentifier> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction/additionalInfo#additionalInfo> a modelldcatno:SimpleType ;
    dct:title "additionalInfo"@en ;
    xsd:maxLength 500 ;
    xsd:minLength 1 ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction/merchant#merchant> a modelldcatno:SimpleType ;
    dct:title "merchant"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Transaction/transactionIdentifier#transactionIdentifier> a modelldcatno:SimpleType ;
    dct:title "transactionIdentifier"@en ;
    xsd:minLength 0 ;
    xsd:maxLength 35 ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/TransactionReference#value> a modelldcatno:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1"^^xsd:nonNegativeInteger ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Amount> a modelldcatno:SimpleType ;
    dct:title "Amount"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#numberschema> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#CounterParty> a modelldcatno:ObjectType ;
    dct:description "Counterparty: the party to which a transaction goes to or comes from"@en ;
    dct:title "CounterParty"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/CounterParty#name> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#TransactionReference> a modelldcatno:ObjectType ;
    dct:title "TransactionReference"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/TransactionReference#value> .
"""

ex_9_ttl = """@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Balance>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#Balance> a modelldcatno:ObjectType ;
    dct:description "Balance: Sum of deposits and loans in the financial account"@en ;
    dct:title "Balance"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Balance#validCurrencies> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Balance#validCurrencies> a modelldcatno:Role ;
    dct:title "validCurrencies"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Balance#validCurrenciesArray> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Balance#validCurrenciesArray> a modelldcatno:ObjectType ;
    dct:title "validCurrenciesArray"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Balance/validCurrencies#items> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f/Balance/validCurrencies#items> a modelldcatno:Attribute ;
    dct:title "items"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/2eb7c51f2a787dedea79ad31f9aff8b474f7097f#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> ."""


ex_10_ttl = """@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111#Balance>,
        <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111#string> .

<http://uri.com> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111#Balance> a modelldcatno:ObjectType ;
    dct:description "Balance: Sum of deposits and loans in the financial account"@en ;
    dct:title "Balance"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111/Balance#validCurrencies> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111/Balance#validCurrencies> a modelldcatno:Role ;
    dct:title "validCurrencies"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasObjectType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111/Balance#validCurrenciesArray> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111/Balance#validCurrenciesArray> a modelldcatno:ObjectType ;
    dct:title "validCurrenciesArray"@en ;
    modelldcatno:hasProperty <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111/Balance/validCurrencies#items> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111/Balance/validCurrencies#items> a modelldcatno:Attribute ;
    dct:title "items"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111#string> .

<https://publishers.staging.fellesdatakatalog.digdir.no/fdk-model-publisher/catalog/5489e4605d1a991ed07a7a271cc75dd3c3222111#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> ."""
