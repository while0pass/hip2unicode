from hip2unicode.functions import hip2unicode as h2u

text = ur'''<::\u043B\u0430\u0442>clav.org

<::\u0441\u043B\u0430\u0432>f~ j\u044C<::\u043B\u0430\u0442>LAT ENGLISH etc. <::\u0441\u043B\u0430\u0432>\u0425\u0440\u005C\u0441\u0442\u0430\u0060\u0020\u0447\u043B\u007E\u0432\u006A\u044C\u043A\u043E\u043B\u044E\u0027\u0431\u0446\u0430\u0020\u0441\u0442\u0440\u005C\u0441\u0442\u0435\u0027\u043C\u044A\u0020\u043F\u043E\u0440\u0435\u0432\u043D\u043E\u0432\u0430\u0027\u0432\u0448\u0435\u0020\u000D\u000A\u0441\u0442\u0440\u005C\u0441\u0442\u043E\u0442\u0435\u0027\u0440\u043F\u0446\u044B\u002C\u0020\u0442\u006A\u044C\u043B\u0435\u0441\u0430\u0060\u0020\u043E\u005F\u0443\u003D\u0027\u0431\u0077\u0020\u043D\u0430\u0020\u0440\u0430\u005E\u043D\u044B\u0020\u043F\u0440\u0435\u0434\u0430\u0027\u0441\u0442\u0435\u002C\u0020\u0438\u003D\u0020\u000D\u000A\u0433\u0077\u0027\u0440\u044C\u043A\u0438\u043C\u044A\u0020\u043C\u0443\u0027\u043A\u0430\u043C\u044A\u002C\u0020\u0442\u044C\u043C\u0430\u0027\u043C\u044A\u0020\u0436\u0435\u0020\u0431\u043E\u043B\u006A\u044C\u0027\u0437\u043D\u0435\u043C\u044A\u002C\u0020\u006A\u0430\u003D\u0027\u043A\u0077\u0020\u000D\u000A\u043F\u0440\u0435\u0434\u0437\u0440\u044F\u0027\u0449\u0435\u0020\u043F\u0440\u0438\u0027\u0441\u043D\u0077\u0020\u0440\u0430\u044F\u0060\u0020\u0431\u0436\u007E\u0435\u0027\u0441\u0442\u0432\u0435\u043D\u043D\u043E\u0435\u0020\u043D\u0430\u0441\u043B\u0430\u0436\u0434\u0435\u0027\u043D\u0069\u0435\u002C\u0020\u043F\u0438\u0027\u0449\u0443\u0020\u000D\u000A\u0436\u0435\u0020\u043D\u0435\u0438\u0436\u0434\u0438\u0432\u0430\u0027\u0435\u043C\u0443\u044E\u0020\u0438\u003D\u0020\u0432\u006A\u044C\u0027\u0447\u043D\u0443\u044E\u0449\u0435\u0435\u0020\u0431\u043B\u007E\u0433\u043E\u0441\u043B\u0430\u0027\u0432\u0069\u0435\u002C\u0020\u005F\u0435\u003D\u0027\u0436\u0435\u0020\u000D\u000A\u043F\u043E\u043B\u0443\u0447\u0438\u0027\u0432\u0448\u0435\u002C\u0020\u043C\u043E\u043B\u0438\u0027\u0442\u0435\u0441\u044F\u0020\u0077\u003D\u0020\u0432\u043E\u0441\u043F\u006A\u044C\u0432\u0430\u0027\u044E\u0449\u0438\u0445\u044A\u0020\u0432\u0430\u0027\u0441\u044A\u002E\u000D\u000A

\u0427\u0435\u0441\u0442\u043D\u0430\u0060\u0020\u0441\u043C\u0435\u0027\u0440\u0442\u044C\u0020\u0441\u0442\u007E\u044B\u0027\u0445\u044A\u0020\u0442\u0432\u043E\u0438\u0027\u0445\u044A\u0020\u0433\u0434\u005C\u0441\u0438\u003A\u0020\u043C\u0435\u0447\u0435\u0027\u043C\u044A\u0020\u0431\u043E\u0020\u0438\u003D\u0020\u000D\u000A\u005F\u043E\u003D\u0433\u043D\u0435\u0027\u043C\u044A\u002C\u0020\u0438\u003D\u0020\u0434\u0443\u0448\u0435\u0027\u044E\u0020\u0441\u043E\u043A\u0440\u0443\u0448\u0435\u0027\u043D\u043D\u043E\u044E\u0020\u043F\u0440\u043E\u043B\u0069\u044F\u0027\u0448\u0430\u0020\u043A\u0440\u0077\u0027\u0432\u0438\u0020\u0441\u0432\u043E\u044F\u005E\u002C\u0020\u000D\u000A\u043E\u005F\u0443\u003D\u043F\u043E\u0432\u0430\u0027\u043D\u0069\u0435\u0020\u0438\u003D\u043C\u0443\u0027\u0449\u0435\u0020\u043D\u0430\u0020\u0442\u044F\u0060\u002C\u0020\u0432\u043E\u0441\u043F\u0440\u0069\u044F\u0027\u0442\u0438\u0020\u0442\u0440\u0443\u0434\u0077\u0027\u0432\u044A\u0020\u043C\u0437\u0434\u0443\u0060\u002C\u0020\u000D\u000A\u0438\u003D\u0020\u043F\u0440\u0435\u0442\u0435\u0440\u043F\u006A\u044C\u0027\u0432\u0448\u0435\u0020\u043F\u0440\u0069\u044F\u0027\u0448\u0430\u0020\u0077\u005C\u0442\u0020\u0442\u0435\u0431\u0435\u0060\u0020\u0441\u043F\u007E\u0441\u0435\u002C\u0020\u0432\u0435\u0027\u043B\u0069\u044E\u0020\u043C\u043B\u005C\u0441\u0442\u044C\u002E\u000D\u000A\u000D\u000A\u0421\u0442\u0069\u0027\u0445\u044A\u003A\u0020\u004A\u0430\u003D\u0027\u043A\u0077\u0020\u043E\u005F\u0443\u003D\u0442\u0432\u0435\u0440\u0434\u0438\u0027\u0441\u044F\u0020\u043C\u043B\u005C\u0441\u0442\u044C\u0020\u005F\u0435\u003D\u0433\u0077\u0060\u0020\u043D\u0430\u0020\u043D\u0430\u0027\u0441\u044A\u0020\u0438\u003D\u0020\u000D\u000A\u0438\u003D\u0027\u0441\u0442\u0438\u043D\u0430\u0020\u0433\u0434\u005C\u0441\u043D\u044F\u0020\u043F\u0440\u0435\u0431\u044B\u0432\u0430\u0027\u0435\u0442\u044A\u0020\u0432\u043E\u0020\u0432\u006A\u044C\u0027\u043A\u044A\u002E'''

converted_text = h2u(text)
hr = '-' * 30

print hr
print text
print hr
print converted_text
print hr
