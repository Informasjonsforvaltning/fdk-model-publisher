"""Example TTL output."""
skagerrak_sparebank_ttl_mock = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://fdk-model-publisher.fellesdatakatalog.no> a dcat:Catalog ;
    dct:title "FDK informasjonsmodellkatalog"@nb ;
    ns1:model <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json> .

<https://fdk-model-publisher.fellesdatakatalog.no#937891245> a foaf:Agent ;
    dct:identifier "937891245" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json> a ns1:InformationModel ;
    dct:conformsTo <https://data.norge.no/specification/kontoopplysninger> ;
    dct:description "Open API specification of the Account APIs. (Work in progress.)"@en ;
    dct:publisher <https://fdk-model-publisher.fellesdatakatalog.no#937891245> ;
    dct:title "Information Model - Accounts API Skagerrak Sparebank"@en ;
    ns1:containsModelElement <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetails>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Accounts>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Cards>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Roles>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transactions> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Account> a ns1:ObjectType ;
    dct:description "Account: a specification of a clearly defined type of financial events"@en ;
    dct:title "Account"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#accountIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#accountReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#currency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#links>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#primaryOwner>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#servicer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#status>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#type> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetails> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "AccountDetails"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#account>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType> a ns1:CodeList ;
    dct:title "AccountPermissionType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> a ns1:CodeList ;
    dct:title "AccountStatus"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Accounts> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Accounts"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#accounts>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#links>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Cards> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Cards"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#paymentCards>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddress> a ns1:ObjectType ;
    dct:title "ElectronicAddress"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#type>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#value> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> a ns1:ObjectType ;
    dct:description "Specific data that assist in identifying the object"@en ;
    dct:title "Identifier"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#countryOfResidence>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#type>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#value> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> a ns1:ObjectType ;
    dct:description "Physical address and location"@en ;
    dct:title "PostalAddress"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#addressLines>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#buildingNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#country>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#postCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#streetName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#townName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#type> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Roles> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Roles"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#responseStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#roles> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transactions> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Transactions"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#links>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#responseStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#transactions> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#accountIdentifier> a ns1:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#accountReference> a ns1:Attribute ;
    dct:title "accountReference"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#links> a ns1:Role ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account/links#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#primaryOwner> a ns1:Role ;
    dct:title "primaryOwner"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#servicer> a ns1:Attribute ;
    dct:title "servicer"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#status> a ns1:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#type> a ns1:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account/links#items> a ns1:ObjectType ;
    dct:description "Pagination: dividing the result into pages for large resultsets"@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#account> a ns1:Attribute ;
    dct:title "account"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#electronicAddresses> a ns1:Role ;
    dct:title "electronicAddresses"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddress> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#endDate> a ns1:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#identifier> a ns1:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#permission> a ns1:Attribute ;
    dct:title "permission"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#postalAddress> a ns1:Role ;
    dct:title "postalAddress"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#startDate> a ns1:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#accounts> a ns1:Role ;
    dct:title "accounts"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Account> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#links> a ns1:Role ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts/links#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts/links#items> a ns1:ObjectType ;
    dct:description "Pagination: dividing the result into pages for large resultsets"@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#paymentCards> a ns1:Role ;
    dct:title "paymentCards"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards/paymentCards#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards/paymentCards#items> a ns1:ObjectType ;
    dct:description "Debit Cards: is the common term for various types of cards used for cash withdrawals and for payment of goods and services at different point of sales"@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#type> a ns1:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#countryOfResidence> a ns1:Attribute ;
    dct:title "countryOfResidence"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#type> a ns1:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#addressLines> a ns1:Role ;
    dct:title "addressLines"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/addressLines#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#buildingNumber> a ns1:Attribute ;
    dct:title "buildingNumber"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#country> a ns1:Attribute ;
    dct:title "country"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#postCode> a ns1:Attribute ;
    dct:description "Post code"@en ;
    dct:title "postCode"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#streetName> a ns1:Attribute ;
    dct:title "streetName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#townName> a ns1:Attribute ;
    dct:title "townName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#type> a ns1:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/addressLines#items> a ns1:ObjectType ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#roles> a ns1:Role ;
    dct:title "roles"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#links> a ns1:Role ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions/links#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#transactions> a ns1:Role ;
    dct:title "transactions"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions/transactions#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions/links#items> a ns1:ObjectType ;
    dct:description "pagination: support division of response for large result sets. The following values should be used: next - For the next page in the transaction set (must be used unless this is the last page), last - indicates the last page of the transaction set. The absence of the next link is interpreted as this being the last page. prev - can be used to specify the previous page. The URL in the links should be relative. "@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions/transactions#items> a ns1:ObjectType ;
    dct:description "transaction: any posting on account"@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> a ns1:ObjectType ;
    dct:description "Account role: indicates owner or manager of account"@en ;
    dct:title "AccountRole"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#electronicAddresses>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#endDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#permission>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#postalAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#startDate> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> a ns1:CodeList ;
    dct:title "ResponseStatus"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> a ns1:SimpleType ;
    dct:title "string"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""
