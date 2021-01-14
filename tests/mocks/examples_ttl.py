"""Example TTL output."""
ex_1_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://www.validuri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - eksempel 1"@nb ;
    ns1:containsModelElement <http://www.validuri.com#Eiendom> .

<http://www.validuri.com#Eiendom> a ns1:ObjectType ;
    dct:title "Eiendom"@en ;
    ns1:hasProperty <http://www.validuri.com#erstatter>,
        <http://www.validuri.com#erstattetav>,
        <http://www.validuri.com#id>,
        <http://www.validuri.com#nummer>,
        <http://www.validuri.com#type> .

<http://www.validuri.com#erstatter> a ns1:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://www.validuri.com#string> .

<http://www.validuri.com#erstattetav> a ns1:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://www.validuri.com#string> .

<http://www.validuri.com#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://www.validuri.com#string> .

<http://www.validuri.com#nummer> a ns1:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://www.validuri.com#string> .

<http://www.validuri.com#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://www.validuri.com#string> .

<http://www.validuri.com#string> a ns1:SimpleType ;
    dct:title "string"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""
