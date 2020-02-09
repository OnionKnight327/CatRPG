from random import randint
from . import item

gameItems = {

    "grumpy":      item.Item("Grumpy", 5, 0, 0, 0, item_type="attitude"),
    "zoomy":       item.Item("Zoomy", 0, 5, 0, 0, item_type="attitude"),
    "inquisitive": item.Item("Inquisitive", 0, 0, 5, 0, item_type="attitude"),
    "brave":       item.Item("Brave", 5, 0, 0, 0, item_type="attitude"),
    "sleepy":      item.Item("Sleepy", -1, -2, -1, 0, item_type="attitude"),
    "stinkyface":  item.Item("Stinkyface", -1, -1, 3, 0, item_type="attitude", move="barf"),
    "nostalgic":   item.Item("Nostalgic", 0, 0, 0, 15, item_type="attitude"),

    "top hat":      item.Item("Top Hat", 3, 3, 3, 15, item_type="hat"),
    "bunny ears":   item.Item("Bunny Ears", 0, 0, 10, 0, item_type="hat", move="bunny"),
    "cat ears":     item.Item("Cat Ears", 5, 5, 5, 15, item_type="hat"),
    "snake hat":    item.Item("Snake Hat", 5, 0, 0, 15, item_type="hat", move="hiss"),
    "fish hat":     item.Item("Fish Hat", 0, 5, 0, 0, item_type="hat", move="splash"),
    "bat hat":      item.Item("Bat Hat", 0, 1, 2, 5, item_type="hat", move="squeak"),

    "gogurt":  item.Item("Gogurt", item_type="quest"),
    "sweater": item.Item("Sweater", item_type="quest"),
    "cat toy": item.Item("Cat Toy", item_type="quest"),
    "mochifood": item.Item("16 Pound Bag of Food", item_type="quest"),

    "potion": item.Item(
        name="Potion",
        item_type="usable",
        item_effect=[["player", "give_hp", randint(1, 8)+1]],
        use_text="You heal a little hp!"
    ),
    "gold star": item.Item(
        name="Gold Star",
        item_type="usable",
        item_effect=[["player", "level_up"]],
        use_text="You get the gold star sticker stuck to your chest fur. You become stronger!"
    ),
    "tuna": item.Item(
        name="Tuna",
        item_type="usable",
        item_effect=[["player", "give_hp", randint(6, 12)+2]],
        use_text="You eat the tuna and gain a bit of HP!"
    ),
    "catnip": item.Item(
        name="Catnip",
        item_type="usable",
        item_effect=[["player", "apply_item", "zoomy"]],
        use_text="You roll around in the catnip and get the zoomies!"
    ),
    "scratcher": item.Item(
        name="Scratching Post",
        item_type="usable",
        item_effect=[["player", "apply_item", "brave"]],
        use_text="You test your claws on the scratching post and shred it to dust! You feel brave!"
    )
}
