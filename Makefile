THEME = dark light
SIZES = 22 24
ICONS = nm-device-wired \
	nm-signal-00 nm-signal-25 nm-signal-50 nm-signal-75 nm-signal-100 \
	gsm-3g-none gsm-3g-low gsm-3g-medium gsm-3g-high gsm-3g-full
PADLOCK = nm-vpn-lock.svg
FILES = $(foreach t,$(THEME),$(foreach s,$(SIZES),$(foreach i,$(ICONS),ubuntu-mono-$t/status/$s/$i-secure.svg)))

all: $(FILES)

%-secure.svg: %.svg 
	./scavenge.py -o $@ $^ $(dir $@)$(PADLOCK)

clean:
	-rm -f $(FILES)

.PHONY: all clean
