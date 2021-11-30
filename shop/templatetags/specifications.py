from django import template
from django.utils.safestring import mark_safe



register = template.Library()


TABLE_HEAD = """
                <table class="table-dark">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr class="table-dark">
                      <td class="table-dark">{name}</td>
                      <td class="table-dark">{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'macbook': {
        'Diagonal': 'diagonal',
        'Display type': 'display_type',
        'Processor freq': 'processor_freq',
        'Ram memory': 'ram',
        'Video adapter': 'video',
        'Time without charge': 'time_without_charge'
    },
    'iphone': {
        'Diagonal': 'diagonal',
        'Display type': 'display_type',
        'Screen resolution': 'resolution',
        'Battery': 'accum_volume',
        'Ram': 'ram',
        'Memory': 'memory',
        'Main camera Mp': 'main_cam_mp',
        'Frontal camera Mp': 'frontal_cam_mp'
    },
     'ipad': {
        'Diagonal': 'diagonal',
        'Display type': 'display_type',
        'Screen resolution': 'resolution',
        'Battery': 'accum_volume',
        'Ram': 'ram',
        'Support apple Pencil': 'penc',
        'Main camera Mp': 'main_cam_mp',
        'Frontal camera Mp': 'frontal_cam_mp'
    },
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
