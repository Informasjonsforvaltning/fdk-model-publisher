"""Example TTL output."""
# flake8: noqa

ex_1_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type ns1:physicalModel ;
    ns1:containsModelElement <http://uri.com#Eiendom> .

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
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#erstattetav> a ns1:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#nummer> a ns1:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_2_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type ns1:physicalModel ;
    ns1:containsModelElement <http://uri.com#Eiendom>,
        <http://uri.com#EiendomResultat> .

<http://uri.com#EiendomResultat> a ns1:ObjectType ;
    dct:title "EiendomResultat"@en ;
    ns1:hasProperty <http://uri.com/EiendomResultat#code>,
        <http://uri.com/EiendomResultat#data>,
        <http://uri.com/EiendomResultat#message> .

<http://uri.com#Int32> a ns1:SimpleType ;
    dct:title "Int32"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com/Eiendom#erstatter> a ns1:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#erstattetav> a ns1:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#nummer> a ns1:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/EiendomResultat#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#Int32> .

<http://uri.com/EiendomResultat#data> a ns1:Role ;
    dct:title "data"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <http://uri.com#Eiendom> .

<http://uri.com/EiendomResultat#message> a ns1:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com#Eiendom> a ns1:ObjectType ;
    dct:title "Eiendom"@en ;
    ns1:hasProperty <http://uri.com/Eiendom#erstatter>,
        <http://uri.com/Eiendom#erstattetav>,
        <http://uri.com/Eiendom#id>,
        <http://uri.com/Eiendom#nummer>,
        <http://uri.com/Eiendom#type> .

<http://uri.com#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_3_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type ns1:physicalModel ;
    ns1:containsModelElement <http://uri.com#Eiendom>,
        <http://uri.com#Kommune>,
        <http://uri.com#SÃ¸k> .

<http://uri.com#Int32> a ns1:SimpleType ;
    dct:title "Int32"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com#SÃ¸k> a ns1:ObjectType ;
    dct:title "SÃ¸k"@en ;
    ns1:hasProperty <http://uri.com/SÃ¸k#code>,
        <http://uri.com/SÃ¸k#data>,
        <http://uri.com/SÃ¸k#message> .

<http://uri.com/Eiendom#erstatter> a ns1:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#erstattetav> a ns1:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#nummer> a ns1:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Kommune#fylke> a ns1:Attribute ;
    dct:title "fylke"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Kommune#gyldigtil> a ns1:Attribute ;
    dct:title "gyldigtil"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" .

<http://uri.com/Kommune#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Kommune#navn> a ns1:Attribute ;
    dct:title "navn"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Kommune#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/SÃ¸k#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#Int32> .

<http://uri.com/SÃ¸k#data> a ns1:Choice ;
    dct:title "data"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "1" ;
    ns1:hasSome <http://uri.com#Eiendom>,
        <http://uri.com#Kommune> .

<http://uri.com/SÃ¸k#message> a ns1:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com#Eiendom> a ns1:ObjectType ;
    dct:title "Eiendom"@en ;
    ns1:hasProperty <http://uri.com/Eiendom#erstatter>,
        <http://uri.com/Eiendom#erstattetav>,
        <http://uri.com/Eiendom#id>,
        <http://uri.com/Eiendom#nummer>,
        <http://uri.com/Eiendom#type> .

<http://uri.com#Kommune> a ns1:ObjectType ;
    dct:title "Kommune"@en ;
    ns1:hasProperty <http://uri.com/Kommune#fylke>,
        <http://uri.com/Kommune#gyldigtil>,
        <http://uri.com/Kommune#id>,
        <http://uri.com/Kommune#navn>,
        <http://uri.com/Kommune#type> .

<http://uri.com#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_4_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type ns1:physicalModel ;
    ns1:containsModelElement <http://uri.com#Eiendom>,
        <http://uri.com#EiendomResultat>,
        <http://uri.com#Kommune>,
        <http://uri.com#KommuneResultat>,
        <http://uri.com#Søk> .

<http://uri.com#EiendomResultat> a ns1:ObjectType ;
    dct:title "EiendomResultat"@en ;
    ns1:hasProperty <http://uri.com/EiendomResultat#code>,
        <http://uri.com/EiendomResultat#data>,
        <http://uri.com/EiendomResultat#message> .

<http://uri.com#Integer> a ns1:SimpleType ;
    dct:title "Integer"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#integerschema> .

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

<http://uri.com/Eiendom#erstatter> a ns1:Attribute ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#erstattetav> a ns1:Attribute ;
    dct:title "erstattetav"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#nummer> a ns1:Attribute ;
    dct:title "nummer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Eiendom#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/EiendomResultat#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#Int32> .

<http://uri.com/EiendomResultat#data> a ns1:Role ;
    dct:title "data"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <http://uri.com#Eiendom> .

<http://uri.com/EiendomResultat#message> a ns1:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Kommune#fylke> a ns1:Attribute ;
    dct:title "fylke"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Kommune#gyldigtil> a ns1:Attribute ;
    dct:title "gyldigtil"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" .

<http://uri.com/Kommune#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Kommune#navn> a ns1:Attribute ;
    dct:title "navn"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/Kommune#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/KommuneResultat#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#Int32> .

<http://uri.com/KommuneResultat#data> a ns1:Composition ;
    dct:title "data"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:contains <http://uri.com/KommuneResultat/data#Data> .

<http://uri.com/KommuneResultat#message> a ns1:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/KommuneResultat/data#Data> a ns1:ObjectType ;
    dct:title "Data"@en ;
    ns1:hasProperty <http://uri.com/KommuneResultat/data/Data#erstatter>,
        <http://uri.com/KommuneResultat/data/Data#erstattetav>,
        <http://uri.com/KommuneResultat/data/Data#kommune> .

<http://uri.com/KommuneResultat/data/Data#erstatter> a ns1:Role ;
    dct:title "erstatter"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Kommune> .

<http://uri.com/KommuneResultat/data/Data#erstattetav> a ns1:Role ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com/KommuneResultat/data/Data/erstattetav/erstattetav#Erstattetav> .

<http://uri.com/KommuneResultat/data/Data#kommune> a ns1:Role ;
    dct:title "kommune"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#Kommune> .

<http://uri.com/KommuneResultat/data/Data/erstattetav/erstattetav#Erstattetav> a ns1:ObjectType ;
    dct:title "Erstattetav"@en ;
    ns1:hasProperty <http://uri.com/KommuneResultat/data/Data/erstattetav/erstattetav/Erstattetav#id> .

<http://uri.com/KommuneResultat/data/Data/erstattetav/erstattetav/Erstattetav#id> a ns1:Attribute ;
    dct:title "id"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#Integer> .

<http://uri.com/Søk#code> a ns1:Attribute ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#Int32> .

<http://uri.com/Søk#data> a ns1:Choice ;
    dct:title "data"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "1" ;
    ns1:hasSome <http://uri.com#Eiendom>,
        <http://uri.com#Kommune> .

<http://uri.com/Søk#message> a ns1:Attribute ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com#Eiendom> a ns1:ObjectType ;
    dct:title "Eiendom"@en ;
    ns1:hasProperty <http://uri.com/Eiendom#erstatter>,
        <http://uri.com/Eiendom#erstattetav>,
        <http://uri.com/Eiendom#id>,
        <http://uri.com/Eiendom#nummer>,
        <http://uri.com/Eiendom#type> .

<http://uri.com#Int32> a ns1:SimpleType ;
    dct:title "Int32"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#integerschema> .

<http://uri.com#Kommune> a ns1:ObjectType ;
    dct:title "Kommune"@en ;
    ns1:hasProperty <http://uri.com/Kommune#fylke>,
        <http://uri.com/Kommune#gyldigtil>,
        <http://uri.com/Kommune#id>,
        <http://uri.com/Kommune#navn>,
        <http://uri.com/Kommune#type> .

<http://uri.com#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_5_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type ns1:physicalModel ;
    ns1:containsModelElement <http://uri.com#Account>,
        <http://uri.com#AccountStatus>,
        <http://uri.com#FinancialInstitution> .

<http://uri.com#Account> a ns1:ObjectType ;
    dct:description "Account: a specification of a clearly defined type of financial events"@en ;
    dct:title "Account"@en ;
    ns1:hasProperty <http://uri.com/Account#servicer>,
        <http://uri.com/Account#status> .

<http://uri.com#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com/Account#servicer> a ns1:Composition ;
    dct:description "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account"@en ;
    dct:title "servicer"@en ;
    ns1:contains <http://uri.com#FinancialInstitution> .

<http://uri.com/Account#status> a ns1:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> ;
    ns1:hasValueFrom <http://uri.com#AccountStatus> .

<http://uri.com/FinancialInstitution#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com/FinancialInstitution/name#String> .

<http://uri.com/FinancialInstitution/name#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 140 ;
    xsd:minLength 1 .

<http://uri.com#AccountStatus> a ns1:CodeList ;
    dct:title "AccountStatus"@en .

<http://uri.com#FinancialInstitution> a ns1:ObjectType ;
    dct:description "financial institution: Business or other institution involved in finance and banking"@en ;
    dct:title "FinancialInstitution"@en ;
    ns1:hasProperty <http://uri.com/FinancialInstitution#name> .
"""

ex_6_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type ns1:physicalModel ;
    ns1:containsModelElement <http://uri.com#ObjA>,
        <http://uri.com#ObjC>,
        <http://uri.com#ObjD> .

<http://uri.com#ObjA> a ns1:ObjectType ;
    dct:description "Root A"@en ;
    dct:title "ObjA"@en ;
    ns1:hasProperty <http://uri.com/ObjA#objB> .

<http://uri.com.well-known/skolem/0> a ns1:Role ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#ObjC> .

<http://uri.com.well-known/skolem/1> a ns1:Role ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#ObjD> .

<http://uri.com.well-known/skolem/2> a ns1:Attribute ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com.well-known/skolem/3> a ns1:Attribute ;
    dct:description "test f"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com/ObjA#objB> a ns1:Composition ;
    dct:description "b thing"@en ;
    dct:title "objB"@en ;
    ns1:contains <http://uri.com/ObjA/objB#ObjB> .

<http://uri.com/ObjA/objB#ObjB> a ns1:ObjectType ;
    ns1:hasProperty <http://uri.com.well-known/skolem/0>,
        <http://uri.com.well-known/skolem/1>,
        <http://uri.com.well-known/skolem/2>,
        <http://uri.com.well-known/skolem/3> .

<http://uri.com#ObjC> a ns1:ObjectType ;
    dct:description "test c"@en ;
    dct:title "ObjC"@en .

<http://uri.com#ObjD> a ns1:ObjectType ;
    dct:description "test d"@en ;
    dct:title "ObjD"@en .

<http://uri.com#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""

ex_7_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type ns1:physicalModel ;
    ns1:containsModelElement <http://uri.com#Balance>,
        <http://uri.com#BalanceType> .

<http://uri.com#Balance> a ns1:ObjectType ;
    dct:description "Balance: Sum of deposits and loans in the financial account"@en ;
    dct:title "Balance"@en ;
    ns1:hasProperty <http://uri.com/Balance#type> .

<http://uri.com/Balance#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasValueFrom <http://uri.com#BalanceType> .

<http://uri.com#BalanceType> a ns1:CodeList ;
    dct:description "Balance type"@en ;
    dct:title "BalanceType"@en .
"""

ex_8_ttl = """
@prefix dct: <http://purl.org/dc/terms/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://uri.com> a ns1:InformationModel ;
    dct:title "Informasjonsmodell - datatjeneste eksempler"@nb ;
    dct:type ns1:physicalModel ;
    ns1:containsModelElement <http://uri.com#CounterParty>,
        <http://uri.com#Transaction>,
        <http://uri.com#TransactionReference> .

<http://uri.com#Amount> a ns1:SimpleType ;
    dct:title "Amount"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#numberschema> .

<http://uri.com#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .

<http://uri.com#Transaction> a ns1:ObjectType ;
    dct:description "Transaction: any posting on an account"@en ;
    dct:title "Transaction"@en ;
    ns1:hasProperty <http://uri.com/Transaction#additionalInfo>,
        <http://uri.com/Transaction#amount>,
        <http://uri.com/Transaction#counterParties>,
        <http://uri.com/Transaction#merchant>,
        <http://uri.com/Transaction#references>,
        <http://uri.com/Transaction#transactionIdentifier> .

<http://uri.com/CounterParty#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com/CounterParty/name#String> .

<http://uri.com/CounterParty/name#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 140 ;
    xsd:minLength 1 .

<http://uri.com/Transaction#additionalInfo> a ns1:Attribute ;
    dct:description "'Additional information on a transaction: textual description of the contents of a transaction'"@en ;
    dct:title "additionalInfo"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com/Transaction/additionalInfo#String> .

<http://uri.com/Transaction#amount> a ns1:Attribute ;
    dct:title "amount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#Amount> .

<http://uri.com/Transaction#counterParties> a ns1:Role ;
    dct:description "Counterparty: another party, the party to whom a transaction is going or coming from"@en ;
    dct:title "counterParties"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#CounterParty> .

<http://uri.com/Transaction#merchant> a ns1:Attribute ;
    dct:description "User location: the physical location of the transaction"@en ;
    dct:title "merchant"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <http://uri.com/Transaction/merchant#String> .

<http://uri.com/Transaction#references> a ns1:Role ;
    dct:description "Transaction reference: unique reference associated with the transaction"@en ;
    dct:title "references"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <http://uri.com#TransactionReference> .

<http://uri.com/Transaction#transactionIdentifier> a ns1:Attribute ;
    dct:description "Transaction Identifier: The identifier for the transaction"@en ;
    dct:title "transactionIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com/Transaction/transactionIdentifier#String> .

<http://uri.com/Transaction/additionalInfo#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 500 ;
    xsd:minLength 1 .

<http://uri.com/Transaction/merchant#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 140 ;
    xsd:minLength 1 .

<http://uri.com/Transaction/transactionIdentifier#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 35 .

<http://uri.com/TransactionReference#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <http://uri.com#String> .

<http://uri.com#CounterParty> a ns1:ObjectType ;
    dct:description "Counterparty: the party to which a transaction goes to or comes from"@en ;
    dct:title "CounterParty"@en ;
    ns1:hasProperty <http://uri.com/CounterParty#name> .

<http://uri.com#TransactionReference> a ns1:ObjectType ;
    dct:title "TransactionReference"@en ;
    ns1:hasProperty <http://uri.com/TransactionReference#value> .
"""
