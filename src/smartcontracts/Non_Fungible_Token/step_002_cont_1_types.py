import smartpy as sp

tstorage = sp.TRecord(admin = sp.TAddress, data = sp.TBigMap(sp.TNat, sp.TRecord(amount = sp.TNat, author = sp.TAddress, collectable = sp.TBool, holder = sp.TAddress, token_id = sp.TNat).layout((("amount", "author"), ("collectable", ("holder", "token_id"))))), metadata = sp.TBigMap(sp.TString, sp.TBytes), token = sp.TAddress, token_id = sp.TNat).layout((("admin", "data"), ("metadata", ("token", "token_id"))))
tparameter = sp.TVariant(collect = sp.TRecord(token_id = sp.TNat).layout("token_id"), collect_management_rewards = sp.TRecord(address = sp.TAddress, amount = sp.TMutez).layout(("address", "amount")), mint = sp.TRecord(amount = sp.TNat, metadata = sp.TBytes).layout(("amount", "metadata")), update_admin = sp.TAddress).layout((("collect", "collect_management_rewards"), ("mint", "update_admin")))
tprivates = { }
tviews = { }
