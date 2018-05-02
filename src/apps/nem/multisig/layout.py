from apps.nem.layout import *
from trezor.messages import NEMAggregateModification
from trezor.messages import NEMModificationType
from trezor.messages import NEMSignTx
from trezor.messages import NEMTransactionCommon
from trezor.crypto import nem


async def ask_multisig(ctx, msg: NEMSignTx):
    address = nem.compute_address(msg.multisig.signer, msg.transaction.network)
    if msg.cosigning:
        await _require_confirm_address(ctx, 'Cosign transaction for', address)
    else:
        await _require_confirm_address(ctx, 'Initiate transaction for', address)
    await require_confirm_fee(ctx, 'Confirm multisig fee', msg.transaction.fee)


async def ask_aggregate_modification(ctx, common: NEMTransactionCommon, mod: NEMAggregateModification, multisig: bool):
    if not multisig:
        await require_confirm_text(ctx, 'Convert account to multisig account?')

    for m in mod.modifications:
        if m.type == NEMModificationType.CosignatoryModification_Add:
            action = 'Add'
        else:
            action = 'Remove'
        address = nem.compute_address(m.public_key, common.network)
        await _require_confirm_address(ctx, action + ' cosignatory', address)

    if mod.relative_change:
        if multisig:
            action = 'Modify the number of cosignatories by '
        else:
            action = 'Set minimum cosignatories to '
        await require_confirm_text(ctx, action + str(mod.relative_change) + '?')

    await require_confirm_final(ctx, common.fee)


async def _require_confirm_address(ctx, action: str, address: str):
    content = Text('Confirm address', ui.ICON_SEND,
                   ui.NORMAL, action,
                   ui.MONO, *split_address(address),
                   icon_color=ui.GREEN)
    await require_confirm(ctx, content, ButtonRequestType.ConfirmOutput)