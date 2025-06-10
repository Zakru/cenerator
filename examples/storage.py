"""
Copyright (c) 2021-2025 Zakru

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import cenerator

p = cenerator.Pack('storage',
    default_namespace='storage',
    description='Cenerator storage example',
    pack_format=71,
)


def print_with_message(c: cenerator.C, message: str, value: cenerator.NumberValue):
    c(f'tellraw @a {{text:"{message}",extra:[{value.to_snbt_text()}]}}')


@p.func(tags = ['minecraft:load'])
def storage(c: cenerator.C):
    stored = c.storage_value('5.6d', 'double')
    print_with_message(c, 'The value is ', stored)
    print_with_message(c, 'The casted value is ', stored.to_storage(c, 'int'))
    print_with_message(c, 'The time is ', c.store_storage('int', 'time query gametime'))
