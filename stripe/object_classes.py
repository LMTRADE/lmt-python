# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_resources


OBJECT_CLASSES = {
    # data structures
    api_resources.ListObject.OBJECT_NAME: api_resources.ListObject,
    api_resources.SearchResultObject.OBJECT_NAME: api_resources.SearchResultObject,
    # business objects
    api_resources.Account.OBJECT_NAME: api_resources.Account,
    api_resources.AccountLink.OBJECT_NAME: api_resources.AccountLink,
    api_resources.AlipayAccount.OBJECT_NAME: api_resources.AlipayAccount,
    api_resources.ApplePayDomain.OBJECT_NAME: api_resources.ApplePayDomain,
    api_resources.ApplicationFee.OBJECT_NAME: api_resources.ApplicationFee,
    api_resources.ApplicationFeeRefund.OBJECT_NAME: api_resources.ApplicationFeeRefund,
    api_resources.Balance.OBJECT_NAME: api_resources.Balance,
    api_resources.BalanceTransaction.OBJECT_NAME: api_resources.BalanceTransaction,
    api_resources.BankAccount.OBJECT_NAME: api_resources.BankAccount,
    api_resources.billing_portal.Configuration.OBJECT_NAME: api_resources.billing_portal.Configuration,
    api_resources.billing_portal.Session.OBJECT_NAME: api_resources.billing_portal.Session,
    api_resources.BitcoinReceiver.OBJECT_NAME: api_resources.BitcoinReceiver,
    api_resources.BitcoinTransaction.OBJECT_NAME: api_resources.BitcoinTransaction,
    api_resources.Capability.OBJECT_NAME: api_resources.Capability,
    api_resources.Card.OBJECT_NAME: api_resources.Card,
    api_resources.Charge.OBJECT_NAME: api_resources.Charge,
    api_resources.checkout.Session.OBJECT_NAME: api_resources.checkout.Session,
    api_resources.CountrySpec.OBJECT_NAME: api_resources.CountrySpec,
    api_resources.Coupon.OBJECT_NAME: api_resources.Coupon,
    api_resources.CreditNote.OBJECT_NAME: api_resources.CreditNote,
    api_resources.CreditNoteLineItem.OBJECT_NAME: api_resources.CreditNoteLineItem,
    api_resources.Customer.OBJECT_NAME: api_resources.Customer,
    api_resources.CustomerBalanceTransaction.OBJECT_NAME: api_resources.CustomerBalanceTransaction,
    api_resources.Dispute.OBJECT_NAME: api_resources.Dispute,
    api_resources.EphemeralKey.OBJECT_NAME: api_resources.EphemeralKey,
    api_resources.Event.OBJECT_NAME: api_resources.Event,
    api_resources.ExchangeRate.OBJECT_NAME: api_resources.ExchangeRate,
    api_resources.File.OBJECT_NAME: api_resources.File,
    api_resources.File.OBJECT_NAME_ALT: api_resources.File,
    api_resources.FileLink.OBJECT_NAME: api_resources.FileLink,
    api_resources.identity.VerificationReport.OBJECT_NAME: api_resources.identity.VerificationReport,
    api_resources.identity.VerificationSession.OBJECT_NAME: api_resources.identity.VerificationSession,
    api_resources.Invoice.OBJECT_NAME: api_resources.Invoice,
    api_resources.InvoiceItem.OBJECT_NAME: api_resources.InvoiceItem,
    api_resources.InvoiceLineItem.OBJECT_NAME: api_resources.InvoiceLineItem,
    api_resources.IssuerFraudRecord.OBJECT_NAME: api_resources.IssuerFraudRecord,
    api_resources.issuing.Authorization.OBJECT_NAME: api_resources.issuing.Authorization,
    api_resources.issuing.Card.OBJECT_NAME: api_resources.issuing.Card,
    api_resources.issuing.CardDetails.OBJECT_NAME: api_resources.issuing.CardDetails,
    api_resources.issuing.Cardholder.OBJECT_NAME: api_resources.issuing.Cardholder,
    api_resources.issuing.Dispute.OBJECT_NAME: api_resources.issuing.Dispute,
    api_resources.issuing.Transaction.OBJECT_NAME: api_resources.issuing.Transaction,
    api_resources.LineItem.OBJECT_NAME: api_resources.LineItem,
    api_resources.LoginLink.OBJECT_NAME: api_resources.LoginLink,
    api_resources.Mandate.OBJECT_NAME: api_resources.Mandate,
    api_resources.Order.OBJECT_NAME: api_resources.Order,
    api_resources.OrderReturn.OBJECT_NAME: api_resources.OrderReturn,
    api_resources.PaymentIntent.OBJECT_NAME: api_resources.PaymentIntent,
    api_resources.PaymentLink.OBJECT_NAME: api_resources.PaymentLink,
    api_resources.PaymentMethod.OBJECT_NAME: api_resources.PaymentMethod,
    api_resources.Payout.OBJECT_NAME: api_resources.Payout,
    api_resources.Person.OBJECT_NAME: api_resources.Person,
    api_resources.Plan.OBJECT_NAME: api_resources.Plan,
    api_resources.Price.OBJECT_NAME: api_resources.Price,
    api_resources.Product.OBJECT_NAME: api_resources.Product,
    api_resources.PromotionCode.OBJECT_NAME: api_resources.PromotionCode,
    api_resources.Quote.OBJECT_NAME: api_resources.Quote,
    api_resources.radar.EarlyFraudWarning.OBJECT_NAME: api_resources.radar.EarlyFraudWarning,
    api_resources.radar.ValueList.OBJECT_NAME: api_resources.radar.ValueList,
    api_resources.radar.ValueListItem.OBJECT_NAME: api_resources.radar.ValueListItem,
    api_resources.Recipient.OBJECT_NAME: api_resources.Recipient,
    api_resources.RecipientTransfer.OBJECT_NAME: api_resources.RecipientTransfer,
    api_resources.Refund.OBJECT_NAME: api_resources.Refund,
    api_resources.reporting.ReportRun.OBJECT_NAME: api_resources.reporting.ReportRun,
    api_resources.reporting.ReportType.OBJECT_NAME: api_resources.reporting.ReportType,
    api_resources.Reversal.OBJECT_NAME: api_resources.Reversal,
    api_resources.Review.OBJECT_NAME: api_resources.Review,
    api_resources.SetupAttempt.OBJECT_NAME: api_resources.SetupAttempt,
    api_resources.SetupIntent.OBJECT_NAME: api_resources.SetupIntent,
    api_resources.ShippingRate.OBJECT_NAME: api_resources.ShippingRate,
    api_resources.sigma.ScheduledQueryRun.OBJECT_NAME: api_resources.sigma.ScheduledQueryRun,
    api_resources.SKU.OBJECT_NAME: api_resources.SKU,
    api_resources.Source.OBJECT_NAME: api_resources.Source,
    api_resources.SourceTransaction.OBJECT_NAME: api_resources.SourceTransaction,
    api_resources.Subscription.OBJECT_NAME: api_resources.Subscription,
    api_resources.SubscriptionItem.OBJECT_NAME: api_resources.SubscriptionItem,
    api_resources.SubscriptionSchedule.OBJECT_NAME: api_resources.SubscriptionSchedule,
    api_resources.TaxCode.OBJECT_NAME: api_resources.TaxCode,
    api_resources.TaxId.OBJECT_NAME: api_resources.TaxId,
    api_resources.TaxRate.OBJECT_NAME: api_resources.TaxRate,
    api_resources.terminal.ConnectionToken.OBJECT_NAME: api_resources.terminal.ConnectionToken,
    api_resources.terminal.Location.OBJECT_NAME: api_resources.terminal.Location,
    api_resources.terminal.Reader.OBJECT_NAME: api_resources.terminal.Reader,
    api_resources.test_helpers.TestClock.OBJECT_NAME: api_resources.test_helpers.TestClock,
    api_resources.ThreeDSecure.OBJECT_NAME: api_resources.ThreeDSecure,
    api_resources.Token.OBJECT_NAME: api_resources.Token,
    api_resources.Topup.OBJECT_NAME: api_resources.Topup,
    api_resources.Transfer.OBJECT_NAME: api_resources.Transfer,
    api_resources.UsageRecord.OBJECT_NAME: api_resources.UsageRecord,
    api_resources.UsageRecordSummary.OBJECT_NAME: api_resources.UsageRecordSummary,
    api_resources.WebhookEndpoint.OBJECT_NAME: api_resources.WebhookEndpoint,
}
