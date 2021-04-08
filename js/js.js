 randomCode: function(e) {
                for (var t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], n = "", i = 0; i < e; i++) {
                    n += t[Math.floor(36 * Math.random())]
                }
                return n

randomCode(12)