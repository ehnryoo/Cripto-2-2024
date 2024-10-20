md5hash(B, A, E, C) {
    if (navigator.userAgent.indexOf("Mozilla/") == 0 && parseInt(navigator.appVersion) >= 4) {
        var D = hex_md5(str_to_ent(trim(B.value)));
        A.value = D;
        if (E) {
            D = hex_md5(trim(B.value));
            E.value = D;
        }
        if (!C) {
            B.value = "";
        }
    }
    return true;
}
