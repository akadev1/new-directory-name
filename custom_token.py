module Token {
    use std::signer;
    use std::vector;

    resource struct Token {
        balance: u64,
    }

    public fun create_token(account: &signer, initial_balance: u64): Token {
        Token { balance: initial_balance }
    }

    public fun get_balance(token: &Token): u64 {
        token.balance
    }

    public fun transfer(sender: &mut Token, receiver: &mut Token, amount: u64) {
        assert!(sender.balance >= amount, 1);
        sender.balance -= amount;
        receiver.balance += amount;
    }
}
