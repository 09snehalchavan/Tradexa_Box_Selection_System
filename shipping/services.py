from decimal import Decimal


def can_fit(product, box):
    dimensions = [
        (product.length, box.length),
        (product.width, box.width),
        (product.height, box.height),
    ]

    product_dimensions = sorted(
        [product.length, product.width, product.height]
    )

    box_dimensions = sorted(
        [box.length, box.width, box.height]
    )

    return (
        all(
            product_dimensions[i] <= box_dimensions[i]
            for i in range(3)
        )
        and product.weight <= box.max_weight
    )


def recommend_box(products, boxes):
    suitable_boxes = []

    total_weight = sum(
        [product.weight for product in products],
        Decimal("0")
    )

    for box in boxes:
        if total_weight <= box.max_weight:
            if all(can_fit(product, box) for product in products):
                suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    return min(suitable_boxes, key=lambda box: box.cost)