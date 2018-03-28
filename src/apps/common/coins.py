from trezor.messages.CoinType import CoinType

# the following list is generated using tools/codegen/gen_coins.py
# do not edit manually!
COINS = [
    CoinType(
        coin_name='Bitcoin',
        coin_shortcut='BTC',
        coin_label='Bitcoin',
        address_type=0,
        address_type_p2sh=5,
        maxfee_kb=2000000,
        signed_message_header='Bitcoin Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix='bc',
        segwit=True,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Testnet',
        coin_shortcut='TEST',
        coin_label='Testnet',
        address_type=111,
        address_type_p2sh=196,
        maxfee_kb=10000000,
        signed_message_header='Bitcoin Signed Message:\n',
        xpub_magic=0x043587cf,
        bech32_prefix='tb',
        segwit=True,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Bcash',
        coin_shortcut='BCH',
        coin_label='Bitcoin Cash',
        address_type=0,
        address_type_p2sh=5,
        maxfee_kb=500000,
        signed_message_header='Bitcoin Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix=None,
        segwit=False,
        forkid=0,
        force_bip143=True,
    ),
    CoinType(
        coin_name='Bcash Testnet',
        coin_shortcut='TBCH',
        coin_label='Bitcoin Cash Testnet',
        address_type=111,
        address_type_p2sh=196,
        maxfee_kb=10000000,
        signed_message_header='Bitcoin Signed Message:\n',
        xpub_magic=0x043587cf,
        bech32_prefix=None,
        segwit=False,
        forkid=0,
        force_bip143=True,
    ),
    CoinType(
        coin_name='Namecoin',
        coin_shortcut='NMC',
        coin_label='Namecoin',
        address_type=52,
        address_type_p2sh=5,
        maxfee_kb=10000000,
        signed_message_header='Namecoin Signed Message:\n',
        xpub_magic=0x019da462,
        bech32_prefix=None,
        segwit=False,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Litecoin',
        coin_shortcut='LTC',
        coin_label='Litecoin',
        address_type=48,
        address_type_p2sh=50,
        maxfee_kb=40000000,
        signed_message_header='Litecoin Signed Message:\n',
        xpub_magic=0x019da462,
        bech32_prefix='ltc',
        segwit=True,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Dogecoin',
        coin_shortcut='DOGE',
        coin_label='Dogecoin',
        address_type=30,
        address_type_p2sh=22,
        maxfee_kb=1000000000,
        signed_message_header='Dogecoin Signed Message:\n',
        xpub_magic=0x02facafd,
        bech32_prefix=None,
        segwit=False,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Dash',
        coin_shortcut='DASH',
        coin_label='Dash',
        address_type=76,
        address_type_p2sh=16,
        maxfee_kb=100000,
        signed_message_header='DarkCoin Signed Message:\n',
        xpub_magic=0x02fe52cc,
        bech32_prefix=None,
        segwit=False,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Zcash',
        coin_shortcut='ZEC',
        coin_label='Zcash',
        address_type=7352,
        address_type_p2sh=7357,
        maxfee_kb=1000000,
        signed_message_header='Zcash Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix=None,
        segwit=False,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Zcash Testnet',
        coin_shortcut='TAZ',
        coin_label='Zcash Testnet',
        address_type=7461,
        address_type_p2sh=7354,
        maxfee_kb=10000000,
        signed_message_header='Zcash Signed Message:\n',
        xpub_magic=0x043587cf,
        bech32_prefix=None,
        segwit=False,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Bitcoin Gold',
        coin_shortcut='BTG',
        coin_label='Bitcoin Gold',
        address_type=38,
        address_type_p2sh=23,
        maxfee_kb=500000,
        signed_message_header='Bitcoin Gold Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix='btg',
        segwit=True,
        forkid=79,
        force_bip143=True,
    ),
    CoinType(
        coin_name='DigiByte',
        coin_shortcut='DGB',
        coin_label='DigiByte',
        address_type=30,
        address_type_p2sh=5,
        maxfee_kb=500000,
        signed_message_header='DigiByte Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix='dgb',
        segwit=True,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Monacoin',
        coin_shortcut='MONA',
        coin_label='Monacoin',
        address_type=50,
        address_type_p2sh=55,
        maxfee_kb=5000000,
        signed_message_header='Monacoin Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix='mona',
        segwit=True,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Fujicoin',
        coin_shortcut='FJC',
        coin_label='Fujicoin',
        address_type=36,
        address_type_p2sh=16,
        maxfee_kb=1000000,
        signed_message_header='FujiCoin Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix=None,
        segwit=False,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Vertcoin',
        coin_shortcut='VTC',
        coin_label='Vertcoin',
        address_type=71,
        address_type_p2sh=5,
        maxfee_kb=40000000,
        signed_message_header='Vertcoin Signed Message:\n',
        xpub_magic=0x0488b21e,
        bech32_prefix='vtc',
        segwit=True,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
        coin_name='Decred Testnet',
        coin_shortcut='TDCR',
        coin_label='Testnet',
        address_type=3873,
        address_type_p2sh=3836,
        maxfee_kb=10000000,
        signed_message_header='Decred Signed Message:\n',
        xpub_magic=0x043587d1,
        bech32_prefix=None,
        segwit=False,
        forkid=None,
        force_bip143=False,
    ),
    CoinType(
         coin_name='Zencash',
         coin_shortcut='ZEN',
         coin_label='Zencash',
         address_type=36,
         address_type_p2sh=5,
         maxfee_kb=2000000,
         minfee_kb=1000,
         signed_message_header='Zencash Signed Message:\n',
         hash_genesis_block='0007104ccda289427919efc39dc9e4d499804b7bebc22df55f8b834301260602',
         xprv_magic=0x0488ade4,
         xpub_magic=0x0488b21e,
         bech32_prefix=None,
         bip44=121,
         segwit=False,
         forkid=None,
         force_bip143=False,
         default_fee_b={'Normal': 10},
         dust_limit=546,
         blocktime_minutes=2.5,
         firmware='stable',
         address_prefix='zencash:',
         min_address_length=35,
         max_address_length=95,
         bitcore=['https://explorer.zensystem.io', 'https://explorer.zen-solutions.io'],
    ),
]


def by_shortcut(shortcut):
    for c in COINS:
        if c.coin_shortcut == shortcut:
            return c
    raise ValueError('Unknown coin shortcut "%s"' % shortcut)


def by_name(name):
    for c in COINS:
        if c.coin_name == name:
            return c
    raise ValueError('Unknown coin name "%s"' % name)


def by_address_type(version):
    for c in COINS:
        if c.address_type == version:
            return c
    raise ValueError('Unknown coin address type %d' % version)
