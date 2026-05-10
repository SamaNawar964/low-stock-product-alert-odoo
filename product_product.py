<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="res_config_settings_view_form_low_stock" model="ir.ui.view">
        <field name="name">res.config.settings.view.form.inherit.low.stocks.product.alert</field>
        <field name="model">res.config.settings</field>
        <field name="inherit_id" ref="stock.res_config_settings_view_form"/>
        <field name="arch" type="xml">
            <xpath expr="//block[@name='product_setting_container']" position="inside">
                <setting id="low_stock_setting" string="Low Stock Alert"
                          help="Change background color for products below the alert quantity">
                    <field name="is_low_stock_alert"/>
                    <div class="content-group" invisible="not is_low_stock_alert">
                        <div class="mt8">
                            <label for="min_low_stock_alert" class="o_light_label"/>
                            <field name="min_low_stock_alert" class="oe_inline"/>
                        </div>
                    </div>
                </setting>
            </xpath>
        </field>
    </record>
</odoo>