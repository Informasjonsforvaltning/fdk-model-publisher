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
    dct:type ns1:physicalModel ;
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

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetail> a ns1:ObjectType ;
    dct:description "Account: a specification of a clearly defined type of financial events"@en ;
    dct:title "AccountDetail"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#accountIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#accountReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#balances>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#currency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#endDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#primaryOwner>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#servicer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#startDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#status>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#type> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetails> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "AccountDetails"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#account>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType> a ns1:CodeList ;
    dct:title "AccountPermissionType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Accounts> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Accounts"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#accounts>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#links>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType> a ns1:CodeList ;
    dct:description "Categorization of ways to use an address according to the type of address the address, as described, is and what you want to do when using the address"@en ;
    dct:title "AddressType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount> a ns1:SimpleType ;
    dct:title "Amount"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#numberschema> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Balance> a ns1:ObjectType ;
    dct:description "Balance: Sum of deposits and loans in the financial account"@en ;
    dct:title "Balance"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#amount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditDebitIndicator>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineAmount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineCurrency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineIncluded>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#currency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#registered>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#type> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BalanceType> a ns1:CodeList ;
    dct:description "Balance type"@en ;
    dct:title "BalanceType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BankTransactionCode> a ns1:ObjectType ;
    dct:description "Transaction code"@en ;
    dct:title "BankTransactionCode"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#domain>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#family>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#freeText>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#subFamily> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Boolean> a ns1:SimpleType ;
    dct:title "Boolean"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#booleanschema> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardType> a ns1:CodeList ;
    dct:description "Card type"@en ;
    dct:title "CardType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Cards> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Cards"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#paymentCards>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterParty> a ns1:ObjectType ;
    dct:description "Counterparty: the party to which a transaction goes to or comes from"@en ;
    dct:title "CounterParty"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#accountIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#postalAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#type> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType> a ns1:CodeList ;
    dct:title "CounterPartyType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode> a ns1:SimpleType ;
    dct:title "CountryCode"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:pattern "[A-Z]{2,2}" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode> a ns1:SimpleType ;
    dct:title "CurrencyCode"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:pattern "[A-Z]{3,3}" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyExchange> a ns1:ObjectType ;
    dct:description "Currency conversion: conversion of an amount from one currency to another"@en ;
    dct:title "CurrencyExchange"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#exchangeRate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#originalAmount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#sourceCurrency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#targetCurrency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#unitCurrency> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> a ns1:CodeList ;
    dct:title "DomainType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddress> a ns1:ObjectType ;
    dct:title "ElectronicAddress"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#type>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#value> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddressType> a ns1:CodeList ;
    dct:title "ElectronicAddressType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> a ns1:CodeList ;
    dct:title "FamilyType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISOYearMonth> a ns1:SimpleType ;
    dct:title "ISOYearMonth"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:pattern "^[0-9]+-([0][1-9]|1[0-2])$" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType> a ns1:CodeList ;
    dct:title "IdentifierType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Number> a ns1:SimpleType ;
    dct:title "Number"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#numberschema> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Roles> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Roles"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#responseStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#roles> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> a ns1:CodeList ;
    dct:title "SubFamilyType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transaction> a ns1:ObjectType ;
    dct:description "Transaction: any posting on an account"@en ;
    dct:title "Transaction"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#additionalInfo>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#amount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#bookingDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#counterParties>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#creditDebitIndicator>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#currency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#currencyExchange>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#merchant>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#paymentCard>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#references>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#registered>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#reversalIndicator>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#status>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#transactionCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#transactionIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#valueDate> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReference> a ns1:ObjectType ;
    dct:title "TransactionReference"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/TransactionReference#type>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/TransactionReference#value> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> a ns1:CodeList ;
    dct:title "TransactionReferenceType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionStatus> a ns1:CodeList ;
    dct:title "TransactionStatus"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transactions> a ns1:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Transactions"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#links>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#responseStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#transactions> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TrueFalseIndicator> a ns1:SimpleType ;
    dct:title "TrueFalseIndicator"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#booleanschema> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#accountIdentifier> a ns1:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#accountReference> a ns1:Attribute ;
    dct:title "accountReference"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#links> a ns1:Role ;
    dct:description "Pagination: dividing the result into pages for large resultsets"@en ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Link> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account/name#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#primaryOwner> a ns1:Role ;
    dct:title "primaryOwner"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#servicer> a ns1:Composition ;
    dct:description "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account"@en ;
    dct:title "servicer"@en ;
    ns1:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FinancialInstitution> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#status> a ns1:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account/name#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 70 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#accountIdentifier> a ns1:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#accountReference> a ns1:Attribute ;
    dct:title "accountReference"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#balances> a ns1:Role ;
    dct:title "balances"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Balance> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#endDate> a ns1:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail/name#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#primaryOwner> a ns1:Role ;
    dct:title "primaryOwner"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#servicer> a ns1:Composition ;
    dct:description "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account"@en ;
    dct:title "servicer"@en ;
    ns1:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FinancialInstitution> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#startDate> a ns1:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#status> a ns1:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail/name#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 70 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#account> a ns1:Composition ;
    dct:title "account"@en ;
    ns1:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetail> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
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
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#identifier> a ns1:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole/name#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#permission> a ns1:Attribute ;
    dct:title "permission"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
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
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole/name#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 140 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#accounts> a ns1:Role ;
    dct:title "accounts"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Account> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#links> a ns1:Role ;
    dct:description "Pagination: dividing the result into pages for large resultsets"@en ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Link> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#amount> a ns1:Attribute ;
    dct:title "amount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditDebitIndicator> a ns1:Attribute ;
    dct:title "creditDebitIndicator"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineAmount> a ns1:Attribute ;
    dct:title "creditLineAmount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineCurrency> a ns1:Attribute ;
    dct:title "creditLineCurrency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineIncluded> a ns1:Attribute ;
    dct:title "creditLineIncluded"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TrueFalseIndicator> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#registered> a ns1:Attribute ;
    dct:title "registered"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BalanceType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#domain> a ns1:Attribute ;
    dct:title "domain"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#family> a ns1:Attribute ;
    dct:title "family"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#freeText> a ns1:Attribute ;
    dct:title "freeText"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode/freeText#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#subFamily> a ns1:Attribute ;
    dct:title "subFamily"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode/freeText#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 500 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#paymentCards> a ns1:Role ;
    dct:description "Debit Cards: is the common term for various types of cards used for cash withdrawals and for payment of goods and services at different point of sales"@en ;
    dct:title "paymentCards"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PaymentCard> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#accountIdentifier> a ns1:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#identifier> a ns1:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty/name#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#postalAddress> a ns1:Role ;
    dct:title "postalAddress"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty/name#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 140 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#exchangeRate> a ns1:Attribute ;
    dct:title "exchangeRate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#originalAmount> a ns1:Attribute ;
    dct:title "originalAmount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Number> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#sourceCurrency> a ns1:Attribute ;
    dct:title "sourceCurrency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#targetCurrency> a ns1:Attribute ;
    dct:title "targetCurrency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#unitCurrency> a ns1:Attribute ;
    dct:title "unitCurrency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddressType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress/value#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress/value#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 2048 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/FinancialInstitution#identifier> a ns1:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/FinancialInstitution#name> a ns1:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/FinancialInstitution/name#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/FinancialInstitution/name#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 140 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#countryOfResidence> a ns1:Attribute ;
    dct:title "countryOfResidence"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link#href> a ns1:Attribute ;
    dct:title "href"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link/href#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link#rel> a ns1:Attribute ;
    dct:title "rel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link/rel#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link/href#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 500 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link/rel#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 50 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIdentifier> a ns1:Attribute ;
    dct:title "cardIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIssuerIdentifier> a ns1:Role ;
    dct:title "cardIssuerIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIssuerName> a ns1:Attribute ;
    dct:description "Card issuers name: The financial institution that has issued a payment card"@en ;
    dct:title "cardIssuerName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard/cardIssuerName#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#expiryDate> a ns1:Attribute ;
    dct:title "expiryDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#holderName> a ns1:Attribute ;
    dct:description "Cardholders name: party to whom the payment card is issued"@en ;
    dct:title "holderName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard/holderName#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#startDate> a ns1:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISOYearMonth> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard/cardIssuerName#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 140 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard/holderName#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 140 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#addressLines> a ns1:Attribute ;
    dct:title "addressLines"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/addressLines#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#buildingNumber> a ns1:Attribute ;
    dct:title "buildingNumber"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/buildingNumber#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#country> a ns1:Attribute ;
    dct:title "country"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#postCode> a ns1:Attribute ;
    dct:description "Post code"@en ;
    dct:title "postCode"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/postCode#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#streetName> a ns1:Attribute ;
    dct:title "streetName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/streetName#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#townName> a ns1:Attribute ;
    dct:title "townName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/townName#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/addressLines#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 70 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/buildingNumber#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 16 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/postCode#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 16 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/streetName#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 70 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/townName#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 35 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#roles> a ns1:Role ;
    dct:title "roles"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#additionalInfo> a ns1:Attribute ;
    dct:description "'Additional information on a transaction: textual description of the contents of a transaction'"@en ;
    dct:title "additionalInfo"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction/additionalInfo#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#amount> a ns1:Attribute ;
    dct:title "amount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#bookingDate> a ns1:Attribute ;
    dct:title "bookingDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#counterParties> a ns1:Role ;
    dct:description "Counterparty: another party, the party to whom a transaction is going or coming from"@en ;
    dct:title "counterParties"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterParty> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#creditDebitIndicator> a ns1:Attribute ;
    dct:title "creditDebitIndicator"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#currency> a ns1:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#currencyExchange> a ns1:Composition ;
    dct:description "Currency conversion: conversion of an amount from one currency to another"@en ;
    dct:title "currencyExchange"@en ;
    ns1:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyExchange> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#merchant> a ns1:Attribute ;
    dct:description "User location: the physical location of the transaction"@en ;
    dct:title "merchant"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction/merchant#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#paymentCard> a ns1:Composition ;
    dct:description "Payment Cards: The common term for various types of cards used for cash withdrawals and for the payment of goods and services at different point of sales"@en ;
    dct:title "paymentCard"@en ;
    ns1:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PaymentCard> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#references> a ns1:Role ;
    dct:description "Transaction reference: unique reference associated with the transaction"@en ;
    dct:title "references"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReference> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#registered> a ns1:Attribute ;
    dct:title "registered"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#reversalIndicator> a ns1:Attribute ;
    dct:title "reversalIndicator"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Boolean> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#status> a ns1:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#transactionCode> a ns1:Composition ;
    dct:description "Transaction code: contains a set of indicators to identify the type of transaction"@en ;
    dct:title "transactionCode"@en ;
    ns1:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BankTransactionCode> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#transactionIdentifier> a ns1:Attribute ;
    dct:description "Transaction Identifier: The identifier for the transaction"@en ;
    dct:title "transactionIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction/transactionIdentifier#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#valueDate> a ns1:Attribute ;
    dct:title "valueDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction/additionalInfo#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 500 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction/merchant#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 140 ;
    xsd:minLength 1 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction/transactionIdentifier#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> ;
    xsd:maxLength 35 .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/TransactionReference#type> a ns1:Attribute ;
    dct:title "type"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/TransactionReference#value> a ns1:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#links> a ns1:Role ;
    dct:description "pagination: support division of response for large result sets. The following values should be used: next - For the next page in the transaction set (must be used unless this is the last page), last - indicates the last page of the transaction set. The absence of the next link is interpreted as this being the last page. prev - can be used to specify the previous page. The URL in the links should be relative. "@en ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Link> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#responseStatus> a ns1:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns1:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> ;
    ns1:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#transactions> a ns1:Role ;
    dct:description "transaction: any posting on account"@en ;
    dct:title "transactions"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns1:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transaction> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> a ns1:CodeList ;
    dct:title "AccountStatus"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> a ns1:CodeList ;
    dct:description "Account type"@en ;
    dct:title "AccountType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit> a ns1:CodeList ;
    dct:title "CreditOrDebit"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FinancialInstitution> a ns1:ObjectType ;
    dct:description "financial institution: Business or other institution involved in finance and banking"@en ;
    dct:title "FinancialInstitution"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/FinancialInstitution#identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/FinancialInstitution#name> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PaymentCard> a ns1:ObjectType ;
    dct:description "debit card: Common term for various types of cards used for cash withdrawals and for payment of goods and services on various point of sales"@en ;
    dct:title "PaymentCard"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIssuerIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIssuerName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#expiryDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#holderName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#startDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#type> .

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

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Link> a ns1:ObjectType ;
    dct:title "Link"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link#href>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link#rel> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> a ns1:ObjectType ;
    dct:description "Specific data that assist in identifying the object"@en ;
    dct:title "Identifier"@en ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#countryOfResidence>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#type>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#value> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> a ns1:CodeList ;
    dct:title "ResponseStatus"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#String> a ns1:SimpleType ;
    dct:title "String"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""
