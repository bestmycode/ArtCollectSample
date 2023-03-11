import smartpy as sp

class Contract(sp.Contract):
  def __init__(self):
    self.init_type(sp.TRecord(admin = sp.TAddress, data = sp.TBigMap(sp.TNat, sp.TRecord(amount = sp.TNat, author = sp.TAddress, collectable = sp.TBool, holder = sp.TAddress, token_id = sp.TNat).layout((("amount", "author"), ("collectable", ("holder", "token_id"))))), metadata = sp.TBigMap(sp.TString, sp.TBytes), token = sp.TAddress, token_id = sp.TNat).layout((("admin", "data"), ("metadata", ("token", "token_id")))))
    self.init(admin = sp.address('tz1UyQDepgtUBnWjyzzonqeDwaiWoQzRKSP5'),
              data = {},
              metadata = {'' : sp.bytes('0x697066733a2f2f516d57386a504d64426d46767353456f4c57505068616f7a4e366a47514678786b77754d4c745646714579364662')},
              token = sp.address('KT1TezoooozzSmartPyzzSTATiCzzzwwBFA1'),
              token_id = 0)

  @sp.entry_point
  def collect(self, params):
    sp.verify((((sp.amount == sp.mul(self.data.data[params.token_id].amount, sp.mutez(1))) & (self.data.data[params.token_id].amount != 0)) & (self.data.data[params.token_id].collectable == True)) & (self.data.data[params.token_id].author != sp.sender))
    self.data.data[params.token_id].collectable = False
    self.data.data[params.token_id].holder = sp.sender
    sp.send(self.data.data[params.token_id].author, sp.split_tokens(sp.amount, 97, 100))
    sp.transfer(sp.list([sp.record(from_ = sp.self_address, txs = sp.list([sp.record(to_ = sp.sender, token_id = params.token_id, amount = 1)]))]), sp.tez(0), sp.contract(sp.TList(sp.TRecord(from_ = sp.TAddress, txs = sp.TList(sp.TRecord(amount = sp.TNat, to_ = sp.TAddress, token_id = sp.TNat).layout(("to_", ("token_id", "amount"))))).layout(("from_", "txs"))), self.data.token, entry_point='transfer').open_some())

  @sp.entry_point
  def collect_management_rewards(self, params):
    sp.verify(sp.sender == self.data.admin)
    sp.send(params.address, params.amount)

  @sp.entry_point
  def mint(self, params):
    sp.verify(params.amount > 0)
    sp.transfer(sp.record(address = sp.self_address, amount = 1, metadata = {'' : params.metadata}, token_id = self.data.token_id), sp.tez(0), sp.contract(sp.TRecord(address = sp.TAddress, amount = sp.TNat, metadata = sp.TMap(sp.TString, sp.TBytes), token_id = sp.TNat).layout((("address", "amount"), ("metadata", "token_id"))), self.data.token, entry_point='mint').open_some())
    self.data.data[self.data.token_id] = sp.record(amount = params.amount, author = sp.sender, collectable = True, holder = sp.self_address, token_id = self.data.token_id)
    self.data.token_id += 1

  @sp.entry_point
  def update_admin(self, params):
    sp.verify(sp.sender == self.data.admin)
    self.data.admin = params

sp.add_compilation_target("test", Contract())