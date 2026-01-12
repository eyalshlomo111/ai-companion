from enum import Enum

class SubscriptionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    CANCELED = "CANCELED"

class LedgerTxType(str, Enum):
    GRANT = "GRANT"
    SPEND = "SPEND"
    EXPIRE = "EXPIRE"
    COMPENSATE = "COMPENSATE"

class CreditSource(str, Enum):
    SUBSCRIPTION_ALLOWANCE = "subscription_allowance"
    WELCOME_BONUS = "welcome_bonus"
    DAILY = "daily"
    WHEEL = "wheel"
    MISSION = "mission"
    PURCHASE = "purchase"
    ADMIN = "admin"

class PremiumActionType(str, Enum):
    UNLOCK_IMAGE = "UNLOCK_IMAGE"
    UNLOCK_VIDEO = "UNLOCK_VIDEO"
    UPGRADE_IMAGE = "UPGRADE_IMAGE"
    UPGRADE_VIDEO = "UPGRADE_VIDEO"
    # Future-safe examples:
    GIFT_PURCHASE = "GIFT_PURCHASE"
    CHARACTER_UNLOCK = "CHARACTER_UNLOCK"

class FulfillmentMode(str, Enum):
    ASYNC_ARTIFACT = "ASYNC_ARTIFACT"
    INSTANT_EFFECT = "INSTANT_EFFECT"

class PremiumActionStatus(str, Enum):
    REQUESTED = "REQUESTED"
    FULFILLING = "FULFILLING"
    READY = "READY"
    CONSUMED = "CONSUMED"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"
