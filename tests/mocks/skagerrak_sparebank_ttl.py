"""Example TTL output."""
skagerrak_sparebank_ttl_mock = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2004/02/skos/core#> .
@prefix ns2: <https://data.norge.no/vocabulary/modelldcatno#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://fdk-model-publisher.fellesdatakatalog.no> a dcat:Catalog ;
    dct:title "FDK informasjonsmodellkatalog"@nb ;
    ns2:model <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json> .

<https://fdk-model-publisher.fellesdatakatalog.no#937891245> a foaf:Agent ;
    dct:identifier "937891245" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json> a ns2:InformationModel ;
    dct:conformsTo <https://data.norge.no/specification/kontoopplysninger> ;
    dct:description "Open API specification of the Account APIs. (Work in progress.)"@en ;
    dct:publisher <https://fdk-model-publisher.fellesdatakatalog.no#937891245> ;
    dct:title "Information Model - Accounts API Skagerrak Sparebank"@en ;
    ns2:containsModelElement <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Account>,
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
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TrueFalseIndicator>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#accountBalancing>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#accountClosing>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#accountManagement>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#accountServicerReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#achDebit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#achReturn>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#achTransactionAtxn>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#achTransactionSala>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#additionalMiscellaneousCreditOperations>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#additionalMiscellaneousDebitOperations>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#adjustments>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#archiveReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#automaticTransfer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#availableBalance>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#bankCheque>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#booked>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#bookedBalance>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#business>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#businessAccount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cashDeposit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cashLetter>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cashManagement>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cashPooling>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cashWithdrawal>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#chargesGeneric>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#chequeNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cheques>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#chequesReversal>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#clientAccount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#commissions>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#complete>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#corporateAction>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#corporateOwnAccountTransfer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#counterTransactions>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#countryIdentificationCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#credit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditAdjustment>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditCard>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditCardPayment>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditTransferWithAgreedCommercialInformation>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditor>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#crossBorderCashWithdrawal>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#crossBorderCheque>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#crossBorderCreditTransfer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#crossBorderIntraCompanyTransfer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#currencyAccount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#customerCardTransactions>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#debit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#debitAdjustmentGeneric>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#debitCard>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#debitCardPayment>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#debtor>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#deleted>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#deliveryTo>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#deposit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#directDebitPayment>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#disabled>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#dividend>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#documentaryCollection>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#domesticCreditTransfer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#drafts>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#emailAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#enabled>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#endToEndIdentification>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#extended>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#fees>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#financialInstitutionCreditTransfer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#foreignExchange>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#info>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#instructionIdentification>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#interestsGeneric>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#intraCompanyTransfer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#invoiceNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#issuedCashConcentrationTransactions>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#issuedCheques>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#issuedCreditTransfers>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#issuedDirectDebits>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#loanAccount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#lockboxTransactions>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#mailTo>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#mandateIdentification>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#merchantCardTransactions>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#messageIdentification>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#miscellaneousCreditOperations>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#miscellaneousDebitOperations>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#nationalIdentityNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#noRight>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#notAvailable>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#openCheque>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#openingAndClosing>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#other>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#otherReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#partial>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#paymentInformationIdentification>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#payments>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#pending>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#phoneNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#pointOfSalePosPayment>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#principalPayment>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#priorityCreditTransfer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#receivedCashConcentrationTransactions>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#receivedCheques>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#receivedCreditTransfers>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#receivedDirectDebits>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#remittanceReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#residential>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#reversalDueToPayment>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#reversalDueToPaymentCancellationRequest>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#reversalDueToPaymentReturn>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#reversalDueToReturnUnpaidDirectDebit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#rightToUseAlone>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#rightToUseWithOther>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#salaryAccount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#sameDayValueCreditTransfer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#savingsAccount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#securities>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#sepaCoreDirectDebit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#sepaCreditTransfer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#settlementAfterCollection>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#settlementAtMaturity>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#standByLetterOfCredit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#standingOrder>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#sweeping>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#taxDeductionAccount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#taxes>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#topping>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#tradeServices>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#travellersChequesDeposit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ultimateCreditor>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ultimateDebtor>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#unpaidCheque>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#valueDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#zeroBalancing> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetails> a ns2:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "AccountDetails"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#account>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountNumber> a ns2:Attribute ;
    dct:description "Account number"@en ;
    dct:title "AccountNumber"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountReference> a ns2:Attribute ;
    dct:description "accountReference - Unique reference to the account. Should not contain sensitive information such as account number"@en ;
    dct:title "AccountReference"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Accounts> a ns2:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Accounts"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#accounts>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#links>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Amount> a ns2:Attribute ;
    dct:description "Amount, always as positive value. CreditDebitIndicator should be used to indicate whether the amount is positive or negative."@en ;
    dct:title "Amount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#number> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardNumber> a ns2:Attribute ;
    dct:description "Masked card number"@en ;
    dct:title "CardNumber"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Cards> a ns2:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Cards"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#paymentCards>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#responseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterParty> a ns2:ObjectType ;
    dct:description "Counterparty: the party to which a transaction goes to or comes from"@en ;
    dct:title "CounterParty"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#accountIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#postalAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#type> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CountryCode> a ns2:Attribute ;
    dct:description "Country code, ISO 3166-1 (alfa-2)"@en ;
    dct:title "CountryCode"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyCode> a ns2:Attribute ;
    dct:title "CurrencyCode"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error> a ns2:ObjectType ;
    dct:description "Error structure for all error messages"@en ;
    dct:title "Error"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error400> a ns2:ObjectType ;
    dct:description "Error structure for error message 400"@en ;
    dct:title "Error400"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error400#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error400#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error401> a ns2:ObjectType ;
    dct:description "Error structure for error message 401"@en ;
    dct:title "Error401"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error401#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error401#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error403> a ns2:ObjectType ;
    dct:description "Error structure for error message 403"@en ;
    dct:title "Error403"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error403#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error403#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error404> a ns2:ObjectType ;
    dct:description "Error structure for error message 404"@en ;
    dct:title "Error404"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error404#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error404#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error405> a ns2:ObjectType ;
    dct:description "Error structure for error message 405"@en ;
    dct:title "Error405"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error405#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error405#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error429> a ns2:ObjectType ;
    dct:description "Error structure for error message 429"@en ;
    dct:title "Error429"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error429#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error429#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Error500> a ns2:ObjectType ;
    dct:description "Error structure for error message 500"@en ;
    dct:title "Error500"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error500#code>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error500#message> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODate> a ns2:Attribute ;
    dct:title "ISODate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISODateTime> a ns2:Attribute ;
    dct:description "ISO DateTime: YYYY-MM-DDThh:mm:ssZ for UTC or YYYY-MM-DDThh:mm:ss+hh for other timezones"@en ;
    dct:title "ISODateTime"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ISOYearMonth> a ns2:Attribute ;
    dct:title "ISOYearMonth"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Link> a ns2:ObjectType ;
    dct:title "Link"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link#href>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link#rel> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Roles> a ns2:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Roles"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#responseStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#roles> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transaction> a ns2:ObjectType ;
    dct:description "Transaction: any posting on an account"@en ;
    dct:title "Transaction"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#additionalInfo>,
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

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReference> a ns2:ObjectType ;
    dct:title "TransactionReference"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/TransactionReference#type>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/TransactionReference#value> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Transactions> a ns2:ObjectType ;
    dct:description "Root element for response"@en ;
    dct:title "Transactions"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#links>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#responseStatus>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#transactions> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TrueFalseIndicator> a ns2:SimpleType ;
    dct:title "TrueFalseIndicator"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#booleanschema> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#accountBalancing> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "accountBalancing" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#accountClosing> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "accountClosing" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#accountManagement> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> ;
    ns1:notation "accountManagement" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#accountServicerReference> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> ;
    ns1:notation "accountServicerReference" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#achDebit> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "achDebit" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#achReturn> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "achReturn" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#achTransactionAtxn> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "achTransactionAtxn" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#achTransactionSala> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "achTransactionSala" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#additionalMiscellaneousCreditOperations> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "additionalMiscellaneousCreditOperations" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#additionalMiscellaneousDebitOperations> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "additionalMiscellaneousDebitOperations" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#adjustments> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "adjustments" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#archiveReference> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> ;
    ns1:notation "archiveReference" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#automaticTransfer> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "automaticTransfer" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#availableBalance> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BalanceType> ;
    ns1:notation "availableBalance" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#bankCheque> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "bankCheque" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#booked> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionStatus> ;
    ns1:notation "booked" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#bookedBalance> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BalanceType> ;
    ns1:notation "bookedBalance" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#business> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType> ;
    ns1:notation "business" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#businessAccount> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> ;
    ns1:notation "businessAccount" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cashDeposit> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "cashDeposit" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cashLetter> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "cashLetter" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cashManagement> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> ;
    ns1:notation "cashManagement" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cashPooling> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "cashPooling" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cashWithdrawal> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "cashWithdrawal" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#chargesGeneric> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "chargesGeneric" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#chequeNumber> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> ;
    ns1:notation "chequeNumber" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#cheques> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "cheques" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#chequesReversal> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "chequesReversal" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#clientAccount> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> ;
    ns1:notation "clientAccount" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#commissions> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "commissions" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#complete> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> ;
    ns1:notation "complete" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#corporateAction> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "corporateAction" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#corporateOwnAccountTransfer> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "corporateOwnAccountTransfer" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#counterTransactions> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "counterTransactions" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#countryIdentificationCode> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType> ;
    ns1:notation "countryIdentificationCode" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#credit> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit> ;
    ns1:notation "credit" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditAdjustment> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "creditAdjustment" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditCard> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardType> ;
    ns1:notation "creditCard" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditCardPayment> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "creditCardPayment" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditTransferWithAgreedCommercialInformation> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "creditTransferWithAgreedCommercialInformation" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#creditor> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType> ;
    ns1:notation "creditor" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#crossBorderCashWithdrawal> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "crossBorderCashWithdrawal" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#crossBorderCheque> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "crossBorderCheque" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#crossBorderCreditTransfer> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "crossBorderCreditTransfer" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#crossBorderIntraCompanyTransfer> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "crossBorderIntraCompanyTransfer" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#currencyAccount> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> ;
    ns1:notation "currencyAccount" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#customerCardTransactions> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "customerCardTransactions" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#debit> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "debit" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#debitAdjustmentGeneric> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "debitAdjustmentGeneric" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#debitCard> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardType> ;
    ns1:notation "debitCard" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#debitCardPayment> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "debitCardPayment" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#debtor> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType> ;
    ns1:notation "debtor" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#deleted> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> ;
    ns1:notation "deleted" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#deliveryTo> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType> ;
    ns1:notation "deliveryTo" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#deposit> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "deposit" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#directDebitPayment> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "directDebitPayment" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#disabled> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> ;
    ns1:notation "disabled" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#dividend> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "dividend" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#documentaryCollection> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "documentaryCollection" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#domesticCreditTransfer> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "domesticCreditTransfer" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#drafts> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "drafts" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#emailAddress> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddressType> ;
    ns1:notation "emailAddress" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#enabled> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> ;
    ns1:notation "enabled" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#endToEndIdentification> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> ;
    ns1:notation "endToEndIdentification" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#extended> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> ;
    ns1:notation "extended" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#fees> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "fees" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#financialInstitutionCreditTransfer> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "financialInstitutionCreditTransfer" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#foreignExchange> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> ;
    ns1:notation "foreignExchange" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#info> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionStatus> ;
    ns1:notation "info" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#instructionIdentification> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> ;
    ns1:notation "instructionIdentification" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#interestsGeneric> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "interestsGeneric" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#intraCompanyTransfer> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "intraCompanyTransfer" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#invoiceNumber> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> ;
    ns1:notation "invoiceNumber" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#issuedCashConcentrationTransactions> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "issuedCashConcentrationTransactions" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#issuedCheques> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "issuedCheques" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#issuedCreditTransfers> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "issuedCreditTransfers" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#issuedDirectDebits> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "issuedDirectDebits" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#loanAccount> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> ;
    ns1:notation "loanAccount" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#lockboxTransactions> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "lockboxTransactions" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#mailTo> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType> ;
    ns1:notation "mailTo" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#mandateIdentification> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> ;
    ns1:notation "mandateIdentification" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#merchantCardTransactions> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "merchantCardTransactions" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#messageIdentification> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> ;
    ns1:notation "messageIdentification" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#miscellaneousCreditOperations> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "miscellaneousCreditOperations" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#miscellaneousDebitOperations> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "miscellaneousDebitOperations" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#nationalIdentityNumber> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType> ;
    ns1:notation "nationalIdentityNumber" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#noRight> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType> ;
    ns1:notation "noRight" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#notAvailable> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "notAvailable" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#openCheque> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "openCheque" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#openingAndClosing> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "openingAndClosing" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#other> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "other" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#otherReference> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> ;
    ns1:notation "otherReference" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#partial> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> ;
    ns1:notation "partial" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#paymentInformationIdentification> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> ;
    ns1:notation "paymentInformationIdentification" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#payments> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> ;
    ns1:notation "payments" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#pending> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionStatus> ;
    ns1:notation "pending" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#phoneNumber> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddressType> ;
    ns1:notation "phoneNumber" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#pointOfSalePosPayment> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "pointOfSalePosPayment" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#principalPayment> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "principalPayment" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#priorityCreditTransfer> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "priorityCreditTransfer" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#receivedCashConcentrationTransactions> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "receivedCashConcentrationTransactions" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#receivedCheques> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "receivedCheques" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#receivedCreditTransfers> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "receivedCreditTransfers" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#receivedDirectDebits> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "receivedDirectDebits" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#remittanceReference> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> ;
    ns1:notation "remittanceReference" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#residential> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType> ;
    ns1:notation "residential" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#reversalDueToPayment> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "reversalDueToPayment" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#reversalDueToPaymentCancellationRequest> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "reversalDueToPaymentCancellationRequest" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#reversalDueToPaymentReturn> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "reversalDueToPaymentReturn" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#reversalDueToReturnUnpaidDirectDebit> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "reversalDueToReturnUnpaidDirectDebit" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#rightToUseAlone> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType> ;
    ns1:notation "rightToUseAlone" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#rightToUseWithOther> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType> ;
    ns1:notation "rightToUseWithOther" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#salaryAccount> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> ;
    ns1:notation "salaryAccount" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#sameDayValueCreditTransfer> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "sameDayValueCreditTransfer" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#savingsAccount> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> ;
    ns1:notation "savingsAccount" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#securities> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> ;
    ns1:notation "securities" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#sepaCoreDirectDebit> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "sepaCoreDirectDebit" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#sepaCreditTransfer> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "sepaCreditTransfer" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#settlementAfterCollection> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "settlementAfterCollection" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#settlementAtMaturity> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "settlementAtMaturity" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#standByLetterOfCredit> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> ;
    ns1:notation "standByLetterOfCredit" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#standingOrder> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "standingOrder" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#sweeping> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "sweeping" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#taxDeductionAccount> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> ;
    ns1:notation "taxDeductionAccount" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#taxes> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "taxes" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#topping> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "topping" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#tradeServices> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> ;
    ns1:notation "tradeServices" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#travellersChequesDeposit> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "travellersChequesDeposit" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ultimateCreditor> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType> ;
    ns1:notation "ultimateCreditor" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ultimateDebtor> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType> ;
    ns1:notation "ultimateDebtor" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#unpaidCheque> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "unpaidCheque" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#valueDate> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "valueDate" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#zeroBalancing> a ns2:CodeElement ;
    ns1:inScheme <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> ;
    ns1:notation "zeroBalancing" .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#accountIdentifier> a ns2:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#accountReference> a ns2:Attribute ;
    dct:title "accountReference"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#currency> a ns2:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#links> a ns2:Role ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account/links#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#name> a ns2:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#primaryOwner> a ns2:Role ;
    dct:title "primaryOwner"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#servicer> a ns2:Composition ;
    dct:description "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account"@en ;
    dct:title "servicer"@en ;
    ns2:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FinancialInstitution> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#status> a ns2:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#type> a ns2:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account/links#items> a ns2:ObjectType ;
    dct:description "Pagination: dividing the result into pages for large resultsets"@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#accountIdentifier> a ns2:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#accountReference> a ns2:Attribute ;
    dct:title "accountReference"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#balances> a ns2:Role ;
    dct:title "balances"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Balance> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#currency> a ns2:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#endDate> a ns2:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#name> a ns2:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#primaryOwner> a ns2:Role ;
    dct:title "primaryOwner"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#servicer> a ns2:Composition ;
    dct:description "account administrator: financial institution that manages an account on behalf of the account owner, including handling the registration of account transactions, calculating the account balance and providing information about the account"@en ;
    dct:title "servicer"@en ;
    ns2:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FinancialInstitution> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#startDate> a ns2:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#status> a ns2:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#type> a ns2:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#account> a ns2:Composition ;
    dct:title "account"@en ;
    ns2:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetail> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetails#responseStatus> a ns2:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#electronicAddresses> a ns2:Role ;
    dct:title "electronicAddresses"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddress> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#endDate> a ns2:Attribute ;
    dct:title "endDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#identifier> a ns2:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#name> a ns2:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#permission> a ns2:Attribute ;
    dct:title "permission"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#postalAddress> a ns2:Role ;
    dct:title "postalAddress"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#startDate> a ns2:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#accounts> a ns2:Role ;
    dct:title "accounts"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Account> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#links> a ns2:Role ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts/links#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts#responseStatus> a ns2:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Accounts/links#items> a ns2:ObjectType ;
    dct:description "Pagination: dividing the result into pages for large resultsets"@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#amount> a ns2:Attribute ;
    dct:title "amount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#number> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditDebitIndicator> a ns2:Attribute ;
    dct:title "creditDebitIndicator"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineAmount> a ns2:Attribute ;
    dct:title "creditLineAmount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#number> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineCurrency> a ns2:Attribute ;
    dct:title "creditLineCurrency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineIncluded> a ns2:Attribute ;
    dct:title "creditLineIncluded"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#boolean> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#currency> a ns2:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#registered> a ns2:Attribute ;
    dct:title "registered"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#type> a ns2:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#domain> a ns2:Attribute ;
    dct:title "domain"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#family> a ns2:Attribute ;
    dct:title "family"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#freeText> a ns2:Attribute ;
    dct:title "freeText"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#subFamily> a ns2:Attribute ;
    dct:title "subFamily"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#paymentCards> a ns2:Role ;
    dct:title "paymentCards"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards/paymentCards#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards#responseStatus> a ns2:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Cards/paymentCards#items> a ns2:ObjectType ;
    dct:description "Debit Cards: is the common term for various types of cards used for cash withdrawals and for payment of goods and services at different point of sales"@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#accountIdentifier> a ns2:Attribute ;
    dct:title "accountIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#identifier> a ns2:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#name> a ns2:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#postalAddress> a ns2:Role ;
    dct:title "postalAddress"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CounterParty#type> a ns2:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#exchangeRate> a ns2:Attribute ;
    dct:title "exchangeRate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#number> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#originalAmount> a ns2:Attribute ;
    dct:title "originalAmount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#number> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#sourceCurrency> a ns2:Attribute ;
    dct:title "sourceCurrency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#targetCurrency> a ns2:Attribute ;
    dct:title "targetCurrency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#unitCurrency> a ns2:Attribute ;
    dct:title "unitCurrency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#type> a ns2:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#value> a ns2:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error#code> a ns2:Attribute ;
    dct:description "error code, for automatic handling"@en ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error#message> a ns2:Attribute ;
    dct:description "description of the error that has occurred"@en ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error400#code> a ns2:Attribute ;
    dct:description "error code, for automatic handling"@en ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error400#message> a ns2:Attribute ;
    dct:description "description of the error event that has occurred"@en ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error401#code> a ns2:Attribute ;
    dct:description "error code, for automatic handling"@en ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error401#message> a ns2:Attribute ;
    dct:description "description of the error that has occurred"@en ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error403#code> a ns2:Attribute ;
    dct:description "error code, for automatic handling"@en ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error403#message> a ns2:Attribute ;
    dct:description "description of the error that has occurred"@en ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error404#code> a ns2:Attribute ;
    dct:description "error code, for automatic handling"@en ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error404#message> a ns2:Attribute ;
    dct:description "description of the error that has occurred"@en ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error405#code> a ns2:Attribute ;
    dct:description "error code, for automatic handling"@en ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error405#message> a ns2:Attribute ;
    dct:description "description of the error that has occurred"@en ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error429#code> a ns2:Attribute ;
    dct:description "error code, for automatic handling"@en ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error429#message> a ns2:Attribute ;
    dct:description "description of the error that has occurred"@en ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error500#code> a ns2:Attribute ;
    dct:description "error code, for automatic handling"@en ;
    dct:title "code"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Error500#message> a ns2:Attribute ;
    dct:description "description of the error that has occurred"@en ;
    dct:title "message"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/FinancialInstitution#identifier> a ns2:Role ;
    dct:title "identifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/FinancialInstitution#name> a ns2:Attribute ;
    dct:title "name"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#countryOfResidence> a ns2:Attribute ;
    dct:title "countryOfResidence"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#type> a ns2:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#value> a ns2:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link#href> a ns2:Attribute ;
    dct:title "href"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Link#rel> a ns2:Attribute ;
    dct:title "rel"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIdentifier> a ns2:Attribute ;
    dct:title "cardIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIssuerIdentifier> a ns2:Role ;
    dct:title "cardIssuerIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIssuerName> a ns2:Attribute ;
    dct:description "Card issuers name: The financial institution that has issued a payment card"@en ;
    dct:title "cardIssuerName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#expiryDate> a ns2:Attribute ;
    dct:title "expiryDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#holderName> a ns2:Attribute ;
    dct:description "Cardholders name: party to whom the payment card is issued"@en ;
    dct:title "holderName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#startDate> a ns2:Attribute ;
    dct:title "startDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#type> a ns2:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#addressLines> a ns2:Role ;
    dct:title "addressLines"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/addressLines#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#buildingNumber> a ns2:Attribute ;
    dct:title "buildingNumber"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#country> a ns2:Attribute ;
    dct:title "country"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#postCode> a ns2:Attribute ;
    dct:description "Post code"@en ;
    dct:title "postCode"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#streetName> a ns2:Attribute ;
    dct:title "streetName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#townName> a ns2:Attribute ;
    dct:title "townName"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#type> a ns2:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress/addressLines#items> a ns2:ObjectType ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#responseStatus> a ns2:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Roles#roles> a ns2:Role ;
    dct:title "roles"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#additionalInfo> a ns2:Attribute ;
    dct:description "'Additional information on a transaction: textual description of the contents of a transaction'"@en ;
    dct:title "additionalInfo"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#amount> a ns2:Attribute ;
    dct:title "amount"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#number> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#bookingDate> a ns2:Attribute ;
    dct:title "bookingDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#counterParties> a ns2:Role ;
    dct:title "counterParties"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction/counterParties#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#creditDebitIndicator> a ns2:Attribute ;
    dct:title "creditDebitIndicator"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#currency> a ns2:Attribute ;
    dct:title "currency"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#currencyExchange> a ns2:Composition ;
    dct:description "Currency conversion: conversion of an amount from one currency to another"@en ;
    dct:title "currencyExchange"@en ;
    ns2:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyExchange> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#merchant> a ns2:Attribute ;
    dct:description "User location: the physical location of the transaction"@en ;
    dct:title "merchant"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "0" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#paymentCard> a ns2:Composition ;
    dct:description "Payment Cards: The common term for various types of cards used for cash withdrawals and for the payment of goods and services at different point of sales"@en ;
    dct:title "paymentCard"@en ;
    ns2:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PaymentCard> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#references> a ns2:Role ;
    dct:title "references"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction/references#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#registered> a ns2:Attribute ;
    dct:title "registered"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#reversalIndicator> a ns2:Attribute ;
    dct:title "reversalIndicator"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#boolean> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#status> a ns2:Attribute ;
    dct:title "status"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#transactionCode> a ns2:Composition ;
    dct:description "Transaction code: contains a set of indicators to identify the type of transaction"@en ;
    dct:title "transactionCode"@en ;
    ns2:contains <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BankTransactionCode> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#transactionIdentifier> a ns2:Attribute ;
    dct:description "Transaction Identifier: The identifier for the transaction"@en ;
    dct:title "transactionIdentifier"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction#valueDate> a ns2:Attribute ;
    dct:title "valueDate"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction/counterParties#items> a ns2:ObjectType ;
    dct:description "Counterparty: another party, the party to whom a transaction is going or coming from"@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transaction/references#items> a ns2:ObjectType ;
    dct:description "Transaction reference: unique reference associated with the transaction"@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/TransactionReference#type> a ns2:CodeList ;
    dct:title "type"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/TransactionReference#value> a ns2:Attribute ;
    dct:title "value"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#links> a ns2:Role ;
    dct:title "links"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions/links#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#responseStatus> a ns2:Attribute ;
    dct:title "responseStatus"@en ;
    xsd:maxOccurs "1" ;
    xsd:minOccurs "1" ;
    ns2:hasSimpleType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> ;
    ns2:hasValueFrom <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions#transactions> a ns2:Role ;
    dct:title "transactions"@en ;
    xsd:maxOccurs "*" ;
    xsd:minOccurs "0" ;
    ns2:hasObjectType <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions/transactions#items> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions/links#items> a ns2:ObjectType ;
    dct:description "pagination: support division of response for large result sets. The following values should be used: next - For the next page in the transaction set (must be used unless this is the last page), last - indicates the last page of the transaction set. The absence of the next link is interpreted as this being the last page. prev - can be used to specify the previous page. The URL in the links should be relative. "@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Transactions/transactions#items> a ns2:ObjectType ;
    dct:description "transaction: any posting on account"@en ;
    dct:title "items"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Account> a ns2:ObjectType ;
    dct:description "Account: a specification of a clearly defined type of financial events"@en ;
    dct:title "Account"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#accountIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#accountReference>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#currency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#links>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#primaryOwner>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#servicer>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#status>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Account#type> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountDetail> a ns2:ObjectType ;
    dct:description "Account: a specification of a clearly defined type of financial events"@en ;
    dct:title "AccountDetail"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountDetail#accountIdentifier>,
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

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Balance> a ns2:ObjectType ;
    dct:description "Balance: Sum of deposits and loans in the financial account"@en ;
    dct:title "Balance"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#amount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditDebitIndicator>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineAmount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineCurrency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#creditLineIncluded>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#currency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#registered>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Balance#type> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BankTransactionCode> a ns2:ObjectType ;
    dct:description "Transaction code"@en ;
    dct:title "BankTransactionCode"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#domain>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#family>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#freeText>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/BankTransactionCode#subFamily> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CurrencyExchange> a ns2:ObjectType ;
    dct:description "Currency conversion: conversion of an amount from one currency to another"@en ;
    dct:title "CurrencyExchange"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#exchangeRate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#originalAmount>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#sourceCurrency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#targetCurrency>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/CurrencyExchange#unitCurrency> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddress> a ns2:ObjectType ;
    dct:title "ElectronicAddress"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#type>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/ElectronicAddress#value> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PaymentCard> a ns2:ObjectType ;
    dct:description "debit card: Common term for various types of cards used for cash withdrawals and for payment of goods and services on various point of sales"@en ;
    dct:title "PaymentCard"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIssuerIdentifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#cardIssuerName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#expiryDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#holderName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#startDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PaymentCard#type> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#boolean> a ns2:SimpleType ;
    dct:title "boolean"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#booleanschema> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#BalanceType> a ns2:CodeList ;
    dct:description "Balance type"@en ;
    dct:title "BalanceType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CardType> a ns2:CodeList ;
    dct:description "Card type"@en ;
    dct:title "CardType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ElectronicAddressType> a ns2:CodeList ;
    dct:title "ElectronicAddressType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FinancialInstitution> a ns2:ObjectType ;
    dct:description "financial institution: Business or other institution involved in finance and banking"@en ;
    dct:title "FinancialInstitution"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/FinancialInstitution#identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/FinancialInstitution#name> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#IdentifierType> a ns2:CodeList ;
    dct:title "IdentifierType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#PostalAddress> a ns2:ObjectType ;
    dct:description "Physical address and location"@en ;
    dct:title "PostalAddress"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#addressLines>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#buildingNumber>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#country>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#postCode>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#streetName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#townName>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/PostalAddress#type> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountRole> a ns2:ObjectType ;
    dct:description "Account role: indicates owner or manager of account"@en ;
    dct:title "AccountRole"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#electronicAddresses>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#endDate>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#identifier>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#name>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#permission>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#postalAddress>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/AccountRole#startDate> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountPermissionType> a ns2:CodeList ;
    dct:title "AccountPermissionType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AddressType> a ns2:CodeList ;
    dct:description "Categorization of ways to use an address according to the type of address the address, as described, is and what you want to do when using the address"@en ;
    dct:title "AddressType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CounterPartyType> a ns2:CodeList ;
    dct:title "CounterPartyType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#CreditOrDebit> a ns2:CodeList ;
    dct:title "CreditOrDebit"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#Identifier> a ns2:ObjectType ;
    dct:description "Specific data that assist in identifying the object"@en ;
    dct:title "Identifier"@en ;
    ns2:hasProperty <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#countryOfResidence>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#type>,
        <https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json/Identifier#value> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionStatus> a ns2:CodeList ;
    dct:title "TransactionStatus"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountStatus> a ns2:CodeList ;
    dct:title "AccountStatus"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#number> a ns2:SimpleType ;
    dct:title "number"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#numberschema> .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#AccountType> a ns2:CodeList ;
    dct:description "Account type"@en ;
    dct:title "AccountType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#ResponseStatus> a ns2:CodeList ;
    dct:title "ResponseStatus"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#DomainType> a ns2:CodeList ;
    dct:title "DomainType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#TransactionReferenceType> a ns2:CodeList ;
    dct:title "TransactionReferenceType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#FamilyType> a ns2:CodeList ;
    dct:title "FamilyType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#SubFamilyType> a ns2:CodeList ;
    dct:title "SubFamilyType"@en .

<https://mockurl.com/Skagerrak_Sparebank_937891245_Accounts-API.json#string> a ns2:SimpleType ;
    dct:title "string"@en ;
    xsd:anyURI <https://www.w3.org/2019/wot/json-schema#stringschema> .
"""
