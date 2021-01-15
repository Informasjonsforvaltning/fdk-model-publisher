"""Example TTL output."""
# flake8: noqa

ex_1_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    ns1:containsModelelement <http://uri.com#Eiendom> .

<http://uri.com#Eiendom> a ns1:ObjectType ;
    dct:title "Eiendom"@en ;
    ns1:hasProperty <http://uri.com/Eiendom#erstatter>,
        <http://uri.com/Eiendom#erstattetav>,
        <http://uri.com/Eiendom#id>,
        <http://uri.com/Eiendom#nummer>,
        <http://uri.com/Eiendom#type> .

<http://uri.com/Eiendom#erstatter> a ns1:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#erstattetav> a ns1:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#nummer> a ns1:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com#string> a ns1:SimpleType ;
    dct:title "string"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_2_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    ns1:containsModelelement <http://uri.com#Eiendom>,
        <http://uri.com#EiendomResultat> .

<http://uri.com#EiendomResultat> a ns1:ObjectType ;
    dct:title "EiendomResultat"@en ;
    ns1:hasProperty <http://uri.com/EiendomResultat#code>,
        <http://uri.com/EiendomResultat#data>,
        <http://uri.com/EiendomResultat#message> .

<http://uri.com#int32> a ns1:SimpleType ;
    dct:title "int32"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com/Eiendom#erstatter> a ns1:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#erstattetav> a ns1:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#nummer> a ns1:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/EiendomResultat#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#int32> .

<http://uri.com/EiendomResultat#data> a ns1:Role ;
    dct:title "data"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <http://uri.com#Eiendom> .

<http://uri.com/EiendomResultat#message> a ns1:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com#Eiendom> a ns1:ObjectType ;
    dct:title "Eiendom"@en ;
    ns1:hasProperty <http://uri.com/Eiendom#erstatter>,
        <http://uri.com/Eiendom#erstattetav>,
        <http://uri.com/Eiendom#id>,
        <http://uri.com/Eiendom#nummer>,
        <http://uri.com/Eiendom#type> .

<http://uri.com#string> a ns1:SimpleType ;
    dct:title "string"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_3_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    ns1:containsModelElement <http://uri.com#Eiendom>,
        <http://uri.com#SÃ¸k> .

<http://uri.com#Kommune> a ns1:ObjectType ;
    dct:title "Kommune"@en .

<http://uri.com#SÃ¸k> a ns1:ObjectType ;
    dct:title "SÃ¸k"@en ;
    ns1:hasProperty <http://uri.com/SÃ¸k#code>,
        <http://uri.com/SÃ¸k#data>,
        <http://uri.com/SÃ¸k#message> .

<http://uri.com#int32> a ns1:SimpleType ;
    dct:title "int32"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com/Eiendom#erstatter> a ns1:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#erstattetav> a ns1:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#nummer> a ns1:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/SÃ¸k#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#int32> .

<http://uri.com/SÃ¸k#data> a ns1:Choice ;
    dct:title "data"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSome <http://uri.com#Eiendom>,
        <http://uri.com#Kommune> .

<http://uri.com/SÃ¸k#message> a ns1:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com#Eiendom> a ns1:ObjectType ;
    dct:title "Eiendom"@en ;
    ns1:hasProperty <http://uri.com/Eiendom#erstatter>,
        <http://uri.com/Eiendom#erstattetav>,
        <http://uri.com/Eiendom#id>,
        <http://uri.com/Eiendom#nummer>,
        <http://uri.com/Eiendom#type> .

<http://uri.com#string> a ns1:SimpleType ;
    dct:title "string"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_4_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    ns1:containsModelelement <http://uri.com#Eiendom>,
        <http://uri.com#EiendomResultat>,
        <http://uri.com#Kommune>,
        <http://uri.com#KommuneResultat>,
        <http://uri.com#Søk> .

<http://uri.com#EiendomResultat> a ns1:ObjectType ;
    dct:title "EiendomResultat"@en ;
    ns1:hasProperty <http://uri.com/EiendomResultat#code>,
        <http://uri.com/EiendomResultat#data>,
        <http://uri.com/EiendomResultat#message> .

<http://uri.com#KommuneResultat> a ns1:ObjectType ;
    dct:title "KommuneResultat"@en ;
    ns1:hasProperty <http://uri.com/KommuneResultat#code>,
        <http://uri.com/KommuneResultat#data>,
        <http://uri.com/KommuneResultat#message> .

<http://uri.com#Søk> a ns1:ObjectType ;
    dct:title "Søk"@en ;
    ns1:hasProperty <http://uri.com/Søk#code>,
        <http://uri.com/Søk#data>,
        <http://uri.com/Søk#message> .

<http://uri.com#erstattetavArray> a ns1:ObjectType ;
    dct:title "erstattetavArray"@en ;
    ns1:hasProperty <http://uri.com#id> .

<http://uri.com#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" .

<http://uri.com/Eiendom#erstatter> a ns1:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#erstattetav> a ns1:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#nummer> a ns1:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/EiendomResultat#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#int32> .

<http://uri.com/EiendomResultat#data> a ns1:Role ;
    dct:title "data"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <http://uri.com#Eiendom> .

<http://uri.com/EiendomResultat#message> a ns1:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#fylke> a ns1:Attribute ;
    dct:title "fylke"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#gyldigtil> a ns1:Attribute ;
    dct:title "gyldigtil"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" .

<http://uri.com/Kommune#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#navn> a ns1:Attribute ;
    dct:title "navn"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/KommuneResultat#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#int32> .

<http://uri.com/KommuneResultat#data> a ns1:ObjectType ;
    dct:title "data"@en ;
    ns1:hasProperty <http://uri.com/KommuneResultat/data#erstatter>,
        <http://uri.com/KommuneResultat/data#erstattetav>,
        <http://uri.com/KommuneResultat/data#kommune> .

<http://uri.com/KommuneResultat#message> a ns1:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com/KommuneResultat/data#erstatter> a ns1:Role ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Kommune> .

<http://uri.com/KommuneResultat/data#erstattetav> a ns1:Role ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#erstattetavArray> .

<http://uri.com/KommuneResultat/data#kommune> a ns1:Role ;
    dct:title "kommune"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Kommune> .

<http://uri.com/Søk#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#int32> .

<http://uri.com/Søk#data> a ns1:Choice ;
    dct:title "data"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSome <http://uri.com#Eiendom>,
        <http://uri.com#Kommune> .

<http://uri.com/Søk#message> a ns1:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#string> .

<http://uri.com#Eiendom> a ns1:ObjectType ;
    dct:title "Eiendom"@en ;
    ns1:hasProperty <http://uri.com/Eiendom#erstatter>,
        <http://uri.com/Eiendom#erstattetav>,
        <http://uri.com/Eiendom#id>,
        <http://uri.com/Eiendom#nummer>,
        <http://uri.com/Eiendom#type> .

<http://uri.com#int32> a ns1:SimpleType ;
    dct:title "int32"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com#Kommune> a ns1:ObjectType ;
    dct:title "Kommune"@en ;
    ns1:hasProperty <http://uri.com/Kommune#fylke>,
        <http://uri.com/Kommune#gyldigtil>,
        <http://uri.com/Kommune#id>,
        <http://uri.com/Kommune#navn>,
        <http://uri.com/Kommune#type> .

<http://uri.com#string> a ns1:SimpleType ;
    dct:title "string"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""
