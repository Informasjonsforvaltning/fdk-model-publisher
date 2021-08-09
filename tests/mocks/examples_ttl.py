"""Example TTL output."""
# flake8: noqa

ex_1_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com.well-known/skolem/0> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <http://uri.com#Eiendom> .

<http://uri.com#Eiendom> a modelldcatno:ObjectType ;
    dct:title "Eiendom"@en ;
    modelldcatno:hasProperty <http://uri.com/Eiendom#erstatter>,
        <http://uri.com/Eiendom#erstattetav>,
        <http://uri.com/Eiendom#id>,
        <http://uri.com/Eiendom#nummer>,
        <http://uri.com/Eiendom#type> .

<http://uri.com.well-known/skolem/0> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<http://uri.com/Eiendom#erstatter> a modelldcatno:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#erstattetav> a modelldcatno:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#nummer> a modelldcatno:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_2_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com.well-known/skolem/0> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <http://uri.com#Eiendom>,
        <http://uri.com#EiendomResultat> .

<http://uri.com#EiendomResultat> a modelldcatno:ObjectType ;
    dct:title "EiendomResultat"@en ;
    modelldcatno:hasProperty <http://uri.com/EiendomResultat#code>,
        <http://uri.com/EiendomResultat#data>,
        <http://uri.com/EiendomResultat#message> .

<http://uri.com#int32> a modelldcatno:SimpleType ;
    dct:title "int32"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com.well-known/skolem/0> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<http://uri.com/Eiendom#erstatter> a modelldcatno:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#erstattetav> a modelldcatno:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#nummer> a modelldcatno:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/EiendomResultat#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#int32> .

<http://uri.com/EiendomResultat#data> a modelldcatno:Role ;
    dct:title "data"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasObjectType <http://uri.com#Eiendom> .

<http://uri.com/EiendomResultat#message> a modelldcatno:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com#Eiendom> a modelldcatno:ObjectType ;
    dct:title "Eiendom"@en ;
    modelldcatno:hasProperty <http://uri.com/Eiendom#erstatter>,
        <http://uri.com/Eiendom#erstattetav>,
        <http://uri.com/Eiendom#id>,
        <http://uri.com/Eiendom#nummer>,
        <http://uri.com/Eiendom#type> .

<http://uri.com#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_3_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com.well-known/skolem/0> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <http://uri.com#Eiendom>,
        <http://uri.com#Kommune>,
        <http://uri.com#SÃ¸k> .

<http://uri.com#SÃ¸k> a modelldcatno:ObjectType ;
    dct:title "SÃ¸k"@en ;
    modelldcatno:hasProperty <http://uri.com/SÃ¸k#code>,
        <http://uri.com/SÃ¸k#data>,
        <http://uri.com/SÃ¸k#message> .

<http://uri.com#date> a modelldcatno:SimpleType ;
    dct:title "date"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com#int32> a modelldcatno:SimpleType ;
    dct:title "int32"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com.well-known/skolem/0> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<http://uri.com/Eiendom#erstatter> a modelldcatno:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#erstattetav> a modelldcatno:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#nummer> a modelldcatno:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#fylke> a modelldcatno:Attribute ;
    dct:title "fylke"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#gyldigtil> a modelldcatno:Attribute ;
    dct:title "gyldigtil"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date> .

<http://uri.com/Kommune#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#navn> a modelldcatno:Attribute ;
    dct:title "navn"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/SÃ¸k#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#int32> .

<http://uri.com/SÃ¸k#data> a modelldcatno:Choice ;
    dct:title "data"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSome <http://uri.com#Eiendom>,
        <http://uri.com#Kommune> .

<http://uri.com/SÃ¸k#message> a modelldcatno:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com#Eiendom> a modelldcatno:ObjectType ;
    dct:title "Eiendom"@en ;
    modelldcatno:hasProperty <http://uri.com/Eiendom#erstatter>,
        <http://uri.com/Eiendom#erstattetav>,
        <http://uri.com/Eiendom#id>,
        <http://uri.com/Eiendom#nummer>,
        <http://uri.com/Eiendom#type> .

<http://uri.com#Kommune> a modelldcatno:ObjectType ;
    dct:title "Kommune"@en ;
    modelldcatno:hasProperty <http://uri.com/Kommune#fylke>,
        <http://uri.com/Kommune#gyldigtil>,
        <http://uri.com/Kommune#id>,
        <http://uri.com/Kommune#navn>,
        <http://uri.com/Kommune#type> .

<http://uri.com#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_4_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com.well-known/skolem/0> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <http://uri.com#Eiendom>,
        <http://uri.com#EiendomResultat>,
        <http://uri.com#Kommune>,
        <http://uri.com#KommuneResultat>,
        <http://uri.com#Søk> .

<http://uri.com#EiendomResultat> a modelldcatno:ObjectType ;
    dct:title "EiendomResultat"@en ;
    modelldcatno:hasProperty <http://uri.com/EiendomResultat#code>,
        <http://uri.com/EiendomResultat#data>,
        <http://uri.com/EiendomResultat#message> .

<http://uri.com#KommuneResultat> a modelldcatno:ObjectType ;
    dct:title "KommuneResultat"@en ;
    modelldcatno:hasProperty <http://uri.com/KommuneResultat#code>,
        <http://uri.com/KommuneResultat#data>,
        <http://uri.com/KommuneResultat#message> .

<http://uri.com#Søk> a modelldcatno:ObjectType ;
    dct:title "Søk"@en ;
    modelldcatno:hasProperty <http://uri.com/Søk#code>,
        <http://uri.com/Søk#data>,
        <http://uri.com/Søk#message> .

<http://uri.com#date> a modelldcatno:SimpleType ;
    dct:title "date"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com#integer> a modelldcatno:SimpleType ;
    dct:title "integer"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com.well-known/skolem/0> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<http://uri.com/Eiendom#erstatter> a modelldcatno:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#erstattetav> a modelldcatno:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#nummer> a modelldcatno:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Eiendom#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/EiendomResultat#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#int32> .

<http://uri.com/EiendomResultat#data> a modelldcatno:Role ;
    dct:title "data"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasObjectType <http://uri.com#Eiendom> .

<http://uri.com/EiendomResultat#message> a modelldcatno:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#fylke> a modelldcatno:Attribute ;
    dct:title "fylke"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#gyldigtil> a modelldcatno:Attribute ;
    dct:title "gyldigtil"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#date> .

<http://uri.com/Kommune#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#navn> a modelldcatno:Attribute ;
    dct:title "navn"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/Kommune#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/KommuneResultat#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#int32> .

<http://uri.com/KommuneResultat#data> a modelldcatno:Composition ;
    dct:title "data"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:contains <http://uri.com/KommuneResultat/data#data> .

<http://uri.com/KommuneResultat#message> a modelldcatno:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com/KommuneResultat/data#data> a modelldcatno:ObjectType ;
    dct:title "data"@en ;
    modelldcatno:hasProperty <http://uri.com/KommuneResultat/data/data#erstatter>,
        <http://uri.com/KommuneResultat/data/data#erstattetav>,
        <http://uri.com/KommuneResultat/data/data#kommune> .

<http://uri.com/KommuneResultat/data/data#erstatter> a modelldcatno:Role ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Kommune> .

<http://uri.com/KommuneResultat/data/data#erstattetav> a modelldcatno:Role ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com/KommuneResultat/data/data/erstattetav#erstattetav> .

<http://uri.com/KommuneResultat/data/data#kommune> a modelldcatno:Role ;
    dct:title "kommune"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#Kommune> .

<http://uri.com/KommuneResultat/data/data/erstattetav#erstattetav> a modelldcatno:ObjectType ;
    dct:title "erstattetav"@en ;
    modelldcatno:hasProperty <http://uri.com/KommuneResultat/data/data/erstattetav/erstattetav#id> .

<http://uri.com/KommuneResultat/data/data/erstattetav/erstattetav#id> a modelldcatno:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#integer> .

<http://uri.com/Søk#code> a modelldcatno:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#int32> .

<http://uri.com/Søk#data> a modelldcatno:Choice ;
    dct:title "data"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSome <http://uri.com#Eiendom>,
        <http://uri.com#Kommune> .

<http://uri.com/Søk#message> a modelldcatno:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com#Eiendom> a modelldcatno:ObjectType ;
    dct:title "Eiendom"@en ;
    modelldcatno:hasProperty <http://uri.com/Eiendom#erstatter>,
        <http://uri.com/Eiendom#erstattetav>,
        <http://uri.com/Eiendom#id>,
        <http://uri.com/Eiendom#nummer>,
        <http://uri.com/Eiendom#type> .

<http://uri.com#int32> a modelldcatno:SimpleType ;
    dct:title "int32"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com#Kommune> a modelldcatno:ObjectType ;
    dct:title "Kommune"@en ;
    modelldcatno:hasProperty <http://uri.com/Kommune#fylke>,
        <http://uri.com/Kommune#gyldigtil>,
        <http://uri.com/Kommune#id>,
        <http://uri.com/Kommune#navn>,
        <http://uri.com/Kommune#type> .

<http://uri.com#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_5_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com.well-known/skolem/0> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <http://uri.com#Account>,
        <http://uri.com#AccountStatus>,
        <http://uri.com#FinancialInstitution> .

<http://uri.com#Account> a modelldcatno:ObjectType ;
    dct:description "Account: a specification of a clearly defined type of financial events"@en ;
    dct:title "Account"@en ;
    modelldcatno:hasProperty <http://uri.com/Account#servicer>,
        <http://uri.com/Account#status> .

<http://uri.com#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com.well-known/skolem/0> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<http://uri.com/Account#servicer> a modelldcatno:Composition ;
    dct:description "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account"@en ;
    dct:title "servicer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:contains <http://uri.com#FinancialInstitution> .

<http://uri.com/Account#status> a modelldcatno:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> ;
    modelldcatno:hasValueFrom <http://uri.com#AccountStatus> .

<http://uri.com/FinancialInstitution#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com/FinancialInstitution/name#name> .

<http://uri.com/FinancialInstitution/name#name> a modelldcatno:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com#AccountStatus> a modelldcatno:CodeList ;
    dct:title "AccountStatus"@en .

<http://uri.com#FinancialInstitution> a modelldcatno:ObjectType ;
    dct:description "financial institution: Business or other institution involved in finance and banking"@en ;
    dct:title "FinancialInstitution"@en ;
    modelldcatno:hasProperty <http://uri.com/FinancialInstitution#name> .
"""

ex_6_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com.well-known/skolem/4> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <http://uri.com#ObjA>,
        <http://uri.com#ObjC>,
        <http://uri.com#ObjD>,
        <http://uri.com#string> .

<http://uri.com#ObjA> a modelldcatno:ObjectType ;
    dct:description "Root A"@en ;
    dct:title "ObjA"@en ;
    modelldcatno:hasProperty <http://uri.com/ObjA#objB> .

<http://uri.com.well-known/skolem/0> a modelldcatno:Role ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#ObjC> .

<http://uri.com.well-known/skolem/1> a modelldcatno:Role ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#ObjD> .

<http://uri.com.well-known/skolem/2> a modelldcatno:Attribute ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com.well-known/skolem/3> a modelldcatno:Attribute ;
    dct:description "test f"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com.well-known/skolem/4> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<http://uri.com/ObjA#objB> a modelldcatno:Composition ;
    dct:description "b thing"@en ;
    dct:title "objB"@en ;
    modelldcatno:contains <http://uri.com/ObjA/objB#objB> .

<http://uri.com/ObjA/objB#objB> a modelldcatno:ObjectType ;
    modelldcatno:hasProperty <http://uri.com.well-known/skolem/0>,
        <http://uri.com.well-known/skolem/1>,
        <http://uri.com.well-known/skolem/2>,
        <http://uri.com.well-known/skolem/3> .

<http://uri.com#ObjC> a modelldcatno:ObjectType ;
    dct:description "test c"@en ;
    dct:title "ObjC"@en .

<http://uri.com#ObjD> a modelldcatno:ObjectType ;
    dct:description "test d"@en ;
    dct:title "ObjD"@en .

<http://uri.com#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_7_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com.well-known/skolem/0> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <http://uri.com#Balance>,
        <http://uri.com#BalanceType> .

<http://uri.com#Balance> a modelldcatno:ObjectType ;
    dct:description "Balance: Sum of deposits and loans in the financial account"@en ;
    dct:title "Balance"@en ;
    modelldcatno:hasProperty <http://uri.com/Balance#type> .

<http://uri.com#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com.well-known/skolem/0> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<http://uri.com/Balance#type> a modelldcatno:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> ;
    modelldcatno:hasValueFrom <http://uri.com#BalanceType> .

<http://uri.com#BalanceType> a modelldcatno:CodeList ;
    dct:description "Balance type"@en ;
    dct:title "BalanceType"@en .
"""

ex_8_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com.well-known/skolem/0> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <http://uri.com#Amount>,
        <http://uri.com#CounterParty>,
        <http://uri.com#Transaction>,
        <http://uri.com#TransactionReference> .

<http://uri.com#Transaction> a modelldcatno:ObjectType ;
    dct:description "Transaction: any posting on an account"@en ;
    dct:title "Transaction"@en ;
    modelldcatno:hasProperty <http://uri.com/Transaction#additionalInfo>,
        <http://uri.com/Transaction#amount>,
        <http://uri.com/Transaction#counterParties>,
        <http://uri.com/Transaction#merchant>,
        <http://uri.com/Transaction#references>,
        <http://uri.com/Transaction#transactionIdentifier> .

<http://uri.com#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com.well-known/skolem/0> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<http://uri.com/CounterParty#name> a modelldcatno:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com/CounterParty/name#name> .

<http://uri.com/CounterParty/name#name> a modelldcatno:SimpleType ;
    dct:title "name"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com/Transaction#additionalInfo> a modelldcatno:Attribute ;
    dct:description "'Additional information on a transaction: textual description of the contents of a transaction'"@en ;
    dct:title "additionalInfo"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com/Transaction/additionalInfo#additionalInfo> .

<http://uri.com/Transaction#amount> a modelldcatno:Attribute ;
    dct:title "amount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#Amount> .

<http://uri.com/Transaction#counterParties> a modelldcatno:Role ;
    dct:description "Counterparty: another party, the party to whom a transaction is going or coming from"@en ;
    dct:title "counterParties"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#CounterParty> .

<http://uri.com/Transaction#merchant> a modelldcatno:Attribute ;
    dct:description "User location: the physical location of the transaction"@en ;
    dct:title "merchant"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com/Transaction/merchant#merchant> .

<http://uri.com/Transaction#references> a modelldcatno:Role ;
    dct:description "Transaction reference: unique reference associated with the transaction"@en ;
    dct:title "references"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasObjectType <http://uri.com#TransactionReference> .

<http://uri.com/Transaction#transactionIdentifier> a modelldcatno:Attribute ;
    dct:description "Transaction Identifier: The identifier for the transaction"@en ;
    dct:title "transactionIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com/Transaction/transactionIdentifier#transactionIdentifier> .

<http://uri.com/Transaction/additionalInfo#additionalInfo> a modelldcatno:SimpleType ;
    dct:title "additionalInfo"@en ;
    xsd:maxLength 500 ;
    xsd:minLength 1 ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com/Transaction/merchant#merchant> a modelldcatno:SimpleType ;
    dct:title "merchant"@en ;
    xsd:maxLength 140 ;
    xsd:minLength 1 ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com/Transaction/transactionIdentifier#transactionIdentifier> a modelldcatno:SimpleType ;
    dct:title "transactionIdentifier"@en ;
    xsd:maxLength 35 ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com/TransactionReference#value> a modelldcatno:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com#Amount> a modelldcatno:SimpleType ;
    dct:title "Amount"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#numberschema> .

<http://uri.com#CounterParty> a modelldcatno:ObjectType ;
    dct:description "Counterparty: the party to which a transaction goes to or comes from"@en ;
    dct:title "CounterParty"@en ;
    modelldcatno:hasProperty <http://uri.com/CounterParty#name> .

<http://uri.com#TransactionReference> a modelldcatno:ObjectType ;
    dct:title "TransactionReference"@en ;
    modelldcatno:hasProperty <http://uri.com/TransactionReference#value> .
"""

ex_9_ttl = """@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix modelldcatno: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a modelldcatno:InformationModel ;
    dct:hasFormat <http://uri.com.well-known/skolem/0> ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type modelldcatno:physicalModel ;
    modelldcatno:containsModelElement <http://uri.com#Balance>,
        <http://uri.com#string> .

<http://uri.com#Balance> a modelldcatno:ObjectType ;
    dct:description "Balance: Sum of deposits and loans in the financial account"@en ;
    dct:title "Balance"@en ;
    modelldcatno:hasProperty <http://uri.com/Balance#validCurrencies> .

<http://uri.com.well-known/skolem/0> a foaf:Document ;
    dct:format "http://publications.europa.eu/resource/authority/file-type/JSON"^^dct:MediaType .

<http://uri.com/Balance#validCurrencies> a modelldcatno:Role ;
    dct:title "validCurrencies"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "1" ;
    modelldcatno:hasObjectType <http://uri.com/Balance#validCurrenciesArray> .

<http://uri.com/Balance#validCurrenciesArray> a modelldcatno:ObjectType ;
    dct:title "validCurrenciesArray"@en ;
    modelldcatno:hasProperty <http://uri.com/Balance/validCurrencies#items> .

<http://uri.com/Balance/validCurrencies#items> a modelldcatno:Attribute ;
    dct:title "items"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    modelldcatno:hasSimpleType <http://uri.com#string> .

<http://uri.com#string> a modelldcatno:SimpleType ;
    dct:title "string"@en ;
    modelldcatno:typeDefinitionReference <https://www.w3.org/2019/wot/json-schema#stringschema> ."""
