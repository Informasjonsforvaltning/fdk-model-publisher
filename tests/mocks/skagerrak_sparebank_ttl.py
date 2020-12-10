skagerrak_sparebank_ttl_mock = """
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <https://data.norge.no/vocabulary/modelldcatno#> .

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
    ns1:containsModelelement <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Account>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetail>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetails>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Accounts>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Balance>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BalanceType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BankTransactionCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Cards>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterParty>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyExchange>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error400>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error401>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error403>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error404>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error405>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error429>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error500>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FinancialInstitution>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODateTime>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISOYearMonth>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Link>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PaymentCard>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Roles>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transaction>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transactions>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TrueFalseIndicator> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Account> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Account"@nb,
        "AccountNumber"@nb,
        "AccountReference"@nb,
        "AccountRole"@nb,
        "AccountType"@nb,
        "AddressType"@nb,
        "CountryCode"@nb,
        "CurrencyCode"@nb,
        "ISODate"@nb,
        "Identifier"@nb,
        "IdentifierType"@nb,
        "PostalAddress"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#addressLines>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#buildingNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#countryOfResidence>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#electronicAddresses>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#links>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#permission>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#postCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#servicer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#status>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#streetName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#townName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetail> a ns1:ModelElement,
        ns1:Property ;
    dct:title "AccountDetail"@nb,
        "AccountNumber"@nb,
        "AccountReference"@nb,
        "AccountRole"@nb,
        "AccountType"@nb,
        "AddressType"@nb,
        "CountryCode"@nb,
        "CurrencyCode"@nb,
        "ISODate"@nb,
        "Identifier"@nb,
        "IdentifierType"@nb,
        "PostalAddress"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#addressLines>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#balances>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#buildingNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#countryOfResidence>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#electronicAddresses>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#permission>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#postCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#servicer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#status>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#streetName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#townName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetails> a ns1:ModelElement,
        ns1:Property ;
    dct:title "AccountDetails"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#account>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType> a ns1:ModelElement ;
    dct:title "AccountPermissionType"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> a ns1:ModelElement ;
    dct:title "AccountStatus"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Accounts> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Accounts"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#accounts>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#links>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Balance> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Amount"@nb,
        "Balance"@nb,
        "BalanceType"@nb,
        "CurrencyCode"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BalanceType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#amount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditDebitIndicator>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditLineIncluded>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#registered> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BalanceType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BankTransactionCode> a ns1:ModelElement,
        ns1:Property ;
    dct:title "BankTransactionCode"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#domain>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#family>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#freeText>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#subFamily> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardNumber> a ns1:ModelElement ;
    dct:title "CardNumber"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Cards> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Cards"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#paymentCards>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterParty> a ns1:ModelElement,
        ns1:Property ;
    dct:title "AccountNumber"@nb,
        "AddressType"@nb,
        "CounterParty"@nb,
        "CounterPartyType"@nb,
        "CountryCode"@nb,
        "Identifier"@nb,
        "IdentifierType"@nb,
        "PostalAddress"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#addressLines>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#buildingNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#countryOfResidence>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#postCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#streetName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#townName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit> a ns1:ModelElement ;
    dct:title "CreditOrDebit"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyExchange> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Amount"@nb,
        "CurrencyExchange"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#originalAmount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#sourceCurrency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#targetCurrency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#unitCurrency> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> a ns1:ModelElement ;
    dct:title "DomainType"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddress> a ns1:ModelElement,
        ns1:Property ;
    dct:title "ElectronicAddress"@nb,
        "ElectronicAddressType"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddressType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Error"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error400> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Error400"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error401> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Error401"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error403> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Error403"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error404> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Error404"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error405> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Error405"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error429> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Error429"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error500> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Error500"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> a ns1:ModelElement ;
    dct:title "FamilyType"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FinancialInstitution> a ns1:ModelElement,
        ns1:Property ;
    dct:title "FinancialInstitution"@nb,
        "Identifier"@nb,
        "IdentifierType"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#countryOfResidence>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODateTime> a ns1:ModelElement ;
    dct:title "ISODateTime"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISOYearMonth> a ns1:ModelElement ;
    dct:title "ISOYearMonth"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Link> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Link"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#href>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#rel> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PaymentCard> a ns1:ModelElement,
        ns1:Property ;
    dct:title "CardType"@nb,
        "Identifier"@nb,
        "IdentifierType"@nb,
        "PaymentCard"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cardIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cardIssuerName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#countryOfResidence>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#expiryDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#holderName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#startDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> a ns1:ModelElement ;
    dct:title "ResponseStatus"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Roles> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Roles"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#responseStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#roles> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> a ns1:ModelElement ;
    dct:title "SubFamilyType"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transaction> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Amount"@nb,
        "CurrencyCode"@nb,
        "Transaction"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#additionalInfo>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#bookingDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#counterParties>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditDebitIndicator>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#currencyExchange>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#merchant>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#paymentCard>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#references>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#registered>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#reversalIndicator>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#status>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#transactionCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#transactionIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#valueDate> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReference> a ns1:ModelElement,
        ns1:Property ;
    dct:title "TransactionReference"@nb,
        "TransactionReferenceType"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionStatus> a ns1:ModelElement ;
    dct:title "TransactionStatus"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transactions> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Transactions"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#links>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#responseStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#transactions> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TrueFalseIndicator> a ns1:ModelElement ;
    dct:title "TrueFalseIndicator"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BalanceType> a ns1:ModelElement ;
    dct:title "BalanceType"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardType> a ns1:ModelElement ;
    dct:title "CardType"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType> a ns1:ModelElement ;
    dct:title "CounterPartyType"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddressType> a ns1:ModelElement ;
    dct:title "ElectronicAddressType"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> a ns1:ModelElement ;
    dct:title "TransactionReferenceType"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountReference> a ns1:ModelElement ;
    dct:title "AccountReference"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> a ns1:ModelElement,
        ns1:Property ;
    dct:title "AccountRole"@nb,
        "AddressType"@nb,
        "CountryCode"@nb,
        "ISODate"@nb,
        "Identifier"@nb,
        "IdentifierType"@nb,
        "PostalAddress"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#addressLines>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#buildingNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#countryOfResidence>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#electronicAddresses>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#permission>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#postCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#streetName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#townName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> a ns1:ModelElement ;
    dct:title "AccountType"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountNumber> a ns1:ModelElement ;
    dct:title "AccountNumber"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount> a ns1:ModelElement ;
    dct:title "Amount"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODate> a ns1:ModelElement ;
    dct:title "ISODate"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode> a ns1:ModelElement ;
    dct:title "CurrencyCode"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> a ns1:ModelElement,
        ns1:Property ;
    dct:title "AddressType"@nb,
        "CountryCode"@nb,
        "PostalAddress"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#addressLines>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#buildingNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#postCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#streetName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#townName> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType> a ns1:ModelElement ;
    dct:title "AddressType"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode> a ns1:ModelElement ;
    dct:title "CountryCode"@nb .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> a ns1:ModelElement,
        ns1:Property ;
    dct:title "Identifier"@nb,
        "IdentifierType"@nb ;
    ns1:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#countryOfResidence>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#value> ;
    ns1:hasType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType> a ns1:ModelElement ;
    dct:title "IdentifierType"@nb .
"""
